# Hubble

Hubble is a modular, open-source security compliance framework built on top of
SaltStack. The project provides on-demand profile-based auditing, real-time
security event notifications, automated remediation, alerting and reporting.
https://hubblestack.io

## Installation (GitFS)

This installation method subscribes directly to our GitHub repository, pinning
to a tag or branch. This method requires no package installation or manual
checkouts.

Requirements: GitFS support on your Salt Master. (Usually just requires
installation of `gitpython` or `pygit2`. `pygit2` is the recommended gitfs
provider.)

*/etc/salt/master.d/hubblestack-nova.conf*

```yaml
fileserver_backend:
  - roots
  - git
gitfs_remotes:
  - https://github.com/hubblestack/hubble-salt.git:
    - base: v2017.4.1
    - root: ''
```

> Remember to restart the Salt Master after applying this change.

You can then run `salt '*' saltutil.sync_all` to sync the modules to your
minions.

See `pillar.example` for sample pillar data for configuring the pulsar beacon
and the splunk/slack returners.

## Schedule

Here is a sample cron file you can drop into cron.d in order to run the jobs
at regular intervals and return the results to splunk:

```bash
# Recommended cron jobs for minions
#
# This file is here for your consumption, but will not automatically be
# deployed by hubble. We recommend you deploy this file on the master at
# /etc/cron.d/hubblestack_cron
#
# If you're worried about master load for running these jobs (most teams won't
# have a problem with this, unless they are several thousand servers per
# master), then use the hubblestack_masterless instructions in this repo
# instead.

MAILTO=""
SHELL=/bin/bash
*/15 * * * * root /usr/bin/salt '*' nebula.queries fifteen_min --return
splunk_nebula_return
@hourly      root /usr/bin/salt '*' nebula.queries hour --return
splunk_nebula_return
@daily       root /usr/bin/salt '*' nebula.queries day --return
splunk_nebula_return
@daily       root /usr/bin/salt '*' cp.cache_file
salt://hubblestack_pulsar/hubblestack_pulsar_config.yaml
@daily       root /usr/bin/salt '*' cp.cache_file
salt://hubblestack_pulsar/hubblestack_pulsar_win_config.yaml
@daily       root /usr/bin/salt '*' hubble.top verbose=True show_profile=True
--return splunk_nova_return
@daily       root /usr/bin/salt '*' saltutil.sync_all
```

## Contribute

If you are interested in contributing or offering feedback to this project feel
free to submit an issue or a pull request. We're very open to community
contribution.


# Nova

## Introduction

Nova is designed to audit the compliance and security level of a system. It is
composed of multiple modules, which ingest YAML configuration profiles to run a
single or series of audits against a system.

## Usage

There are four primary functions in the hubble.py module:

1. `hubble.sync` will sync the `hubblestack_nova_profiles/` and `hubblestack_nova/` directories to the minion(s).
2. `hubble.load` will load the synced audit modules and their yaml configuration files.
3. `hubble.audit` will audit the minion(s) using the YAML profile(s) you provide as comma-separated arguments
4. `hubble.top` will audit the minion(s) using the `top.nova` configuration.

`hubble.audit` takes two optional arguments. The first is a comma-separated
list of paths.  These paths can be files or directories within the
`hubblestack_nova_profiles` directory. The second argument allows for
toggling Nova configuration, such as verbosity, level of detail, etc.

If `hubble.audit` is run without targeting any audit configs or directories,
it will instead run `hubble.top` with no arguments.

`hubble.audit` will return a list of audits which were successful, and a list
of audits which failed.

Here are some example calls:

```bash
# Run the cve scanner and the CIS profile:
salt \* hubble.audit cve.scan-v2,cis.centos-7-level-1-scored-v1

# Run hubble.top with the default topfile (top.nova)
salt \* hubble.top

# Run all yaml configs and tags under salt://hubblestack_nova_profiles/foo/
# and salt://hubblestack_nova_profiles/bar, but only run audits with tags
# starting with "CIS"
salt \* hubble.audit foo,bar tags='CIS*'
```

## Nova Topfiles

Nova topfiles look very similar to saltstack topfiles, except the top-level
key is always `nova`, as nova doesn't have environments.

```yaml
nova:
  '*':
    - cve.scan-v2
    - network.ssh
    - network.smtp
  'web*':
    - cis.centos-7-level-1-scored-v1
    - cis.centos-7-level-2-scored-v1
  'G@os_family:debian':
    - network.ssh
    - cis.debian-7-level-1-scored: 'CIS*'
```

Additionally, all nova topfile matches are compound matches, so you never
need to define a match type like you do in saltstack topfiles.

Each list item is a string representing the dot-separated location of a
yaml file which will be run with hubble.audit. You can also specify a
tag glob to use as a filter for just that yaml file, using a colon
after the yaml file (turning it into a dictionary). See the last two lines
in the yaml above for examples.

Examples:

```bash
salt '*' hubble.top
salt '*' hubble.top foo/bar/top.nova
salt '*' hubble.top foo/bar.nova verbose=True
```

## Compensating Control Configuration

In some cases, your organization may want to skip certain audit checks for
certain hosts. This is supported via compensating control configuration.

You can skip a check globally by adding a `control: <reason>` key to the check
itself. This key should be added at the same level as `description` and
`trigger` pieces of a check. In this case, the check will never run, and will
output under the `Controlled` results key.

Nova also supports separate control profiles, for more fine-grained control
using topfiles. You can use a separate YAML top-level key called `control`.
Generally, you'll put this top-level key inside of a separate YAML file and
only include it in the top-data for the hosts for which it is relevant.

For these separate control configs, the audits will always run, whether they
are controlled or not. However, controlled audits which fail will be converted
from `Failure` to `Controlled` in a post-processing operation.

The control config syntax is as follows:

```yaml
control:
  - CIS-2.1.4: This is the reason we control the check
  - some_other_tag:
      reason: This is the reason we control the check
  - a_third_tag_with_no_reason
```

Note that providing a reason for the control is optional. Any of the three
formats shown in the yaml list above will work.

Once you have your compensating control config, just target the yaml to the
hosts you want to control using your topfile. In this case, all the audits will
still run, but if any of the controlled checks fail, they will be removed from
`Failure` and added to `Controlled`, and will be treated as a Success for
the purposes of compliance percentage.

## Configuration

1. The directory/environment in which nova searches for audit modules are
configurable via pillar. The defaults are shown below:

```yaml
hubblestack:
  nova:
    saltenv: base
    module_dir: salt://hubblestack_nova
    profile_dir: salt://hubblestack_nova_profiles
```

2. By default, `hubble.audit` will call `hubble.load` (which in turn calls
`hubble.sync`) in order to ensure that it is auditing with the most up-to-date
information. These operations are fairly fast, but if you want to avoid the
additional overhead, you can disable these behaviors via pillar (defaults are
shown, change to False to disable behaviors):


```yaml
hubblestack:
  nova:
    autosync: True
    autoload: True
```

## Development

If you're interested in contributing to this project this section outlines the
structure and requirements for Nova audit module development.

### Anatomy of a Nova audit module

```python
# -*- encoding: utf-8 -*-
'''
Loader and primary interface for nova modules

:maintainer: HubbleStack
:maturity: 20160214
:platform: Linux
:requires: SaltStack

'''
from __future__ import absolute_import
import logging
```

All Nova plugins should include the above header, expanding the docstring to
include full documentation

```python
import fnmatch
import salt.utils

def __virtual__():
    if salt.utils.is_windows():
        return False, 'This audit module only runs on linux'
    return True


def audit(data_list, tag, debug=False):
    __tags__ = []
    for profile, data in data_list:
        # This is where you process the dictionaries passed in by hubble.py,
        # searching for data pertaining to this audit module. Modules which
        # require no data should use yaml which is empty except for a
        # top-level key, and should only do work if the top-level key is
        # found in the data

        # We need to also inject the profile # in the data for each check so
        # that it appears in verbose output
        pass

    ret = {'Success': [], 'Failure': []}
    for tag in __tags__:
        if fnmatch.fnmatch(tag, tags):
            # We should run this tag
            # <do audit stuff here>
            ret['Success'].append(tag)
    return ret
```

All Nova plugins require a `__virtual__()` function to determine module
compatibility, and an `audit()` function to perform the actual audit
functionality

The `audit()` function must take three arguments, `data_list`, `tag`, and
`debug`. The `data_list` argument is a list of dictionaries passed in by
`hubble.py`. `hubble.py` gets this data from loading the specified yaml for the
audit run. Your audit module should only run if it finds its own data in this
list. The `tag` argument is a glob expression for which tags the audit function
should run. It is the job of the audit module to compare the `tag` glob with
all tags supported by this module and only run the audits which match. The
`debug` argument tells whether the module should log additional debugging
information at debug log level.

The return value should be a dictionary, with optional keys "Success",
"Failure", and "Controlled". The values for these keys should be a list of
one-key dictionaries in the form of `{<tag>: <string_description>}`, or a
list of one-key dictionaries in the form of `{<tag>: <data_dict>}` (in the
case of `verbose`).


# Nebula

## Introduction

Nebula is Hubble's Insight system, which ties into ``osquery``, allowing you to
query your infrastructure as if it were a database. This system can be used to
take scheduled snapshots of your systems.

Note: Currently only supported on SaltStack 2015.8 and above. You can actually
sync the osquery execution module from a newer version of salt to 2015.5
minions and it seems to work without issue. Officially, just upgrade to 2015.8.

Nebula has a semi-hard dependency on the ``osqueryi`` binary. See install
requirements here https://osquery.io/downloads/

## Usage

These queries have been designed to give detailed insight into system activity.

`hubblestack_nebula/hubblestack_nebula_queries.yaml`

```yaml
fifteen_min:
  - query_name: running_procs
    query: SELECT p.name AS process, p.pid AS process_id, p.cmdline, p.cwd, p.on_disk, p.resident_size AS mem_used, p.parent, g.groupname, u.username AS user, p.path, h.md5, h.sha1, h.sha256 FROM processes AS p LEFT JOIN users AS u ON p.uid=u.uid LEFT JOIN groups AS g ON p.gid=g.gid LEFT JOIN hash AS h ON p.path=h.path;
  - query_name: established_outbound
    query: SELECT t.iso_8601 AS _time, pos.family, h.*, ltrim(pos.local_address, ':f') AS src, pos.local_port AS src_port, pos.remote_port AS dest_port, ltrim(remote_address, ':f') AS dest, name, p.path AS file_path, cmdline, pos.protocol, lp.protocol FROM process_open_sockets AS pos JOIN processes AS p ON p.pid=pos.pid LEFT JOIN time AS t LEFT JOIN (SELECT * FROM listening_ports) AS lp ON lp.port=pos.local_port AND lp.protocol=pos.protocol LEFT JOIN hash AS h ON h.path=p.path WHERE NOT remote_address='' AND NOT remote_address='::' AND NOT remote_address='0.0.0.0' AND NOT remote_address='127.0.0.1' AND port is NULL;
  - query_name: listening_procs
    query:  SELECT t.iso_8601 AS _time, h.md5 AS md5, p.pid, name, ltrim(address, ':f') AS address, port, p.path AS file_path, cmdline, root, parent FROM listening_ports AS lp LEFT JOIN processes AS p ON lp.pid=p.pid LEFT JOIN time AS t LEFT JOIN hash AS h ON h.path=p.path WHERE NOT address='127.0.0.1';
  - query_name: suid_binaries
    query: SELECT sb.*, t.iso_8601 AS _time FROM suid_bin AS sb JOIN time AS t;
hour:
  - query_name: crontab
    query: SELECT c.*,t.iso_8601 AS _time FROM crontab AS c JOIN time AS t;
day:
  - query_name: rpm_packages
    query: SELECT rpm.name, rpm.version, rpm.release, rpm.source AS package_source, rpm.size, rpm.sha1, rpm.arch, t.iso_8601 FROM rpm_packages AS rpm JOIN time AS t;
```

## Configuration

The only configuration required to use Nebula is to incorporate the Queries and
the Schedule into your minion config or pillar (pillar recommended). See the
Usage section above for more information.

Nebula leverages the ``osquery_nebula`` execution module, which needs to be
synced to each minion. In addition, this also requires the ``osquery`` binary
to be installed.

More information about osquery can be found at https://osquery.io.

Note: ``osqueryd`` does not need to be running, as we handle the scheduled
queries via the cron jobs.


# Pulsar

Note: After syncing a new version of a beacon to salt, the salt-minion
must be restarted to pick up the change. See
https://github.com/saltstack/salt/issues/35960 for more info

## Introduction

Pulsar is designed to monitor for file system events, acting as a real-time
File Integrity Monitoring (FIM) agent. Pulsar is composed of a custom Salt
beacon that watches for these events and hooks into the returner system for
alerting and reporting.

In other words, you can recieve real-time alerts for unscheduled file system
modifications *anywhere* you want to recieve them.

We've designed Pulsar to be lightweight and not dependent on a Salt Master. It
simply watches for events and directly sends them to one of the Pulsar
returner destinations (see Quasar for more on these).

## Usage

Once Pulsar is fully running there isn't anything you need to do to interact
with it. It simply runs quietly in the background and sends you alerts.

## Configuration

The default Pulsar configuration (found in ``<pillar.example>``)
is meant to act as a template. It works in tandem with the
``<hubblestack_pulsar_config.yaml>`` file. Every environment will have
different needs and requirements, and we understand that, so we've designed
Pulsar to be flexible.

** pillar.example **

```yaml
beacons:
  pulsar:
    paths:
      - /var/cache/salt/minion/files/base/hubblestack_pulsar/hubblestack_pulsar_config.yaml
schedule:
  cache_pulsar:
    function: cp.cache_file
    seconds: 86400
    args:
      - salt://hubblestack_pulsar/hubblestack_pulsar_config.yaml
    return_job: False
```

** hubblestack_pulsar_config **

```yaml
/etc: { recurse: True, auto_add: True }
/bin: { recurse: True, auto_add: True }
/sbin: { recurse: True, auto_add: True }
/boot: { recurse: True, auto_add: True }
/usr/bin: { recurse: True, auto_add: True }
/usr/sbin: { recurse: True, auto_add: True }
/usr/local/bin: { recurse: True, auto_add: True }
/usr/local/sbin: { recurse: True, auto_add: True }
return: slack_pulsar
checksum: sha256
stats: True
batch: False
```

In order to receive Pulsar notifications you'll need to install the custom
returners found in the Quasar_ repository.

Example of using the Slack Pulsar returner to recieve FIM notifications:

```yaml
slack_pulsar:
  as_user: true
  username: calculon
  channel: hubble_pulsar
  api_key: xoxo-xxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx
```

Tip: If you need to create a Slack bot, see: https://my.slack.com/services/new/bot

### Excluding Paths

There may be certain paths that you want to exclude from this real-time
FIM tool. This can be done using the ``exclude:`` keyword beneath any
defined path.

```yaml
/var:
  recurse: True
  auto_add: True
  exclude:
    - /var/log
    - /var/spool
    - /var/cache
    - /var/lock
```


## Troubleshooting

If inotify is reporting that it can't create watches due to lack of disk space,
but you have plenty of disk space and inodes available, then you may have to
raise the max number of inotify watches.

To check the max number of inotify watches:

```bash
cat /proc/sys/fs/inotify/max_user_watches
```

To set the max number of inotify watches:

```bash
echo 20000 | sudo tee -a /proc/sys/fs/inotify/max_user_watches
```


## Under The Hood

Pulsar is written as a Salt beacon, which requires the ``salt-minion`` daemon
to be running. This then acts as an agent that watches for file system events
using Linux's ``inotify`` subsystem.


# Quasar

## Introduction

Quasar is Hubble's reporting system; a key component in visualizing your data.
Quasar gathers the data captured by Nova, Nebula and Pulsar and delivers it
directly to your logging or SIM/SEM system. Create dashboards, alerts and
correlations all using the SIM/SEM system you already have!

Note: dashboards not included :)

## Usage

Each Quasar module has different requirements and settings. Please see your preferred module's documentation.
