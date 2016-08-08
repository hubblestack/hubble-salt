osquery
-------

==========  ====================
maintainer  HubbleStack
maturity    2016.7.0
platform    Unix
requires    SaltStack_, :doc:`HubbleStack Nebula<../../../nebula/README>`, osquery_
source      https://github.com/HubbleStack/Nebula/blob/master/_modules/nebula_osquery.py
==========  ====================

.. _SaltStack: https://saltstack.com
.. _osquery: https://osquery.io

This module leverages the data made available via ``osquery`` in order to
generate security snapshots of your systems. These snapshots are generally run
on a schedule, with the data being gathered centrally using one of the
:doc:`Quasar<../../../quasar/README>` returners.

Configuration
~~~~~~~~~~~~~

This module requires pillar data to function. The default pillar key for
this data is ``nebula_osquery``.  The queries themselves should be grouped
under one or more group identifiers. Usually, these identifiers will be
frequencies, such as ``fifteen_min`` or ``hourly`` or ``daily``. The module
targets the queries using these identifiers.

Your pillar data might look like this:

**hubble_nebula.sls**

.. code-block:: yaml
   :linenos:


    nebula_osquery:
      fifteen_min:
        - query_name: running_procs
          query: select p.name as process, p.pid as process_id, p.cmdline, p.cwd, p.on_disk, p.resident_size as mem_used, p.parent, g.groupname, u.username as user, p.path, h.md5, h.sha1, h.sha256 from processes as p left join users as u on p.uid=u.uid left join groups as g on p.gid=g.gid left join hash as h on p.path=h.path;
        - query_name: established_outbound
          query: select t.iso_8601 as _time, pos.family, h.*, ltrim(pos.local_address, ':f') as src, pos.local_port as src_port, pos.remote_port as dest_port, ltrim(remote_address, ':f') as dest, name, p.path as file_path, cmdline, pos.protocol, lp.protocol from process_open_sockets as pos join processes as p on p.pid=pos.pid left join time as t LEFT JOIN listening_ports as lp on lp.port=pos.local_port AND lp.protocol=pos.protocol LEFT JOIN hash as h on h.path=p.path where not remote_address='' and not remote_address='::' and not remote_address='0.0.0.0' and not remote_address='127.0.0.1' and port is NULL;
        - query_name: listening_procs
          query:  select t.iso_8601 as _time, h.md5 as md5, p.pid, name, ltrim(address, ':f') as address, port, p.path as file_path, cmdline, root, parent from listening_ports as lp JOIN processes as p on lp.pid=p.pid left JOIN time as t JOIN hash as h on h.path=p.path WHERE not address='127.0.0.1';
        - query_name: suid_binaries
          query: select sb.*, t.iso_8601 as _time from suid_bin as sb join time as t;
      hour:
        - query_name: crontab
          query: select c.*,t.iso_8601 as _time from crontab as c join time as t;
      day:
        - query_name: rpm_packages
          query: select rpm.*, t.iso_8601 from rpm_packages as rpm join time as t;

Schedule
~~~~~~~~

The Nebula osquery module is designed to be used on a schedule. Here is a set
of sample schedules for use with the sample pillar data contained in this repo:

**hubble_nebula.sls (cont.)**

.. code-block:: yaml
   :linenos:


    schedule:
      nebula_fifteen_min:
        function: nebula.queries
        seconds: 900
        args:
          - fifteen_min
      nebula_hour:
        function: nebula.queries
        seconds: 3600
        args:
          - hour
      nebula_day:
        function: nebula.queries
        seconds: 86400
        args:
          - day

.. note:: ``osqueryd`` does not need to be running, as we handle the scheduled queries via Salt's scheduler.
