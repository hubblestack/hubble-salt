Pulsar Beacon
=============

Pulsar was written to leverage ``inotify`` to watch for file system events in
real-time. This allows a system running the Pulsar Beacon to notify you on
unscheduled file system changes. This can be used to not only track out-of-band
changes, but potentially catch intrusions as they happen.

When a file system event is triggered, Pulsar will notify you of the type of
change (``IN_CREATE``, ``IN_MODIFY`` or ``IN_DELETE``), and provide you with
information about the changed file. This includes checksums of the events as
well as file attributes, such as permissions, ownerships, paths, etc.

The Pulsar beacon is enabled by installing the beacon module and providing the
beacon with pillar configuration data.

Configuration
-------------

Pulsar configuration supports a handful of options which are outlined below:

.. code-block:: yaml

    beacons:
      pulsar:
        /etc: { recurse: True, auto_add: True }
        /lib: { recurse: True, auto_add: True }
        /bin: { recurse: True, auto_add: True }
        /sbin: { recurse: True, auto_add: True }
        /boot: { recurse: True, auto_add: True }
        /lib64: { recurse: True, auto_add: True }
        /usr/lib: { recurse: True, auto_add: True }
        /usr/bin: { recurse: True, auto_add: True }
        /usr/sbin: { recurse: True, auto_add: True }
        /usr/lib64: { recurse: True, auto_add: True }
        /usr/local/etc: { recurse: True, auto_add: True }
        /usr/local/bin: { recurse: True, auto_add: True }
        /usr/local/lib: { recurse: True, auto_add: True }
        /usr/local/sbin: { recurse: True, auto_add: True }
        /var:
          exclude:
            - /var/log
            - /var/spool
            - /var/cache
            - /var/lock
            - /var/lib/ntp
            - /var/lib/chrony
            - /var/lib/mlocate
            - /var/lib/logrotate.status
          recurse: True
          audo_add: True
        return: slack_pulsar
        checksum: sha256
        stats: True
        batch: False

The majority of the options contained within the Pulsar beacon config are
simply paths that you'd like the system to watch. The options of ``recurse``
and ``auto_add`` will ensure that subdirectories are tracked and newly added
files watched.

Another crucial option is the ``exclude`` key, which allows you to exclude
specific subdirectories. Be careful not to exclude *too* much or you may end up
with blindspots.

In addition the ``return`` option allows you to specify a comma-separated list
of returners. In the example above we're using the ``slack_pulsar`` returner.
One of the custom Pulsar returners must be used in order to properly recieve
these alerts.  

To learn more about the custom returners please see the Quasar_ repo.

.. _Quasar: https://github.com/hubblestack/quasar
