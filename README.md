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
    - base: v2017.3.1
    - root: ''
```

> Remember to restart the Salt Master after applying this change.

You can then run `salt '*' saltutil.sync_all` to sync the modules to your
minions.

See `pillar.example` for sample pillar data for configuring the pulsar beacon
and the splunk/slack returners.
