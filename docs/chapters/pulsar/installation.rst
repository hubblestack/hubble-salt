Pulsar
======

Pulsar is Hubble's event notification system. This component is a configured
set of Salt beacons and reactors that can notify you on any defined schedule
when file system events occur. Example configuration files are found in the
HubbleStack Pulsar repository:

.. code-block:: shell

    $ git clone https://github.com/HubbleStack/Pulsar.git hubblestack-pulsar.git

Currently there are two supported methods for watching for FIM alerts. The
first is a combination of compared checksums on a schedule. The second is a
beacon-based real-time notification system. Recreate the `inotify` structure
found within the `pulsar` directory within your `file_roots`.

There are plans to make this (and other) custom modules into SPM packages. This
will allow for simpler installation and management.
