Hubble
======

Hubble at it's core is a flexible loader system masquerading as a SaltStack
execution module.

Early on in developing this suite of tools it became obvious that we would
overrun the SaltStack `modules` directory if we were to create custom auditing
execution modules directly into SaltStack. We needed another solution to
organize the suite of auditing tools that we were building. With that we
decided to extend the Salt loader system by way of a drop-in execution module
that allows for loading a suite of external modules.

The hope here is that integration with SaltStack (upstream) will be as simple
as dropping in a custom execution module. After that the loader will do the
heavy lifting and modules can be developed separately.

Under the Hood
--------------

The Hubble loader system scans for plugins in four different places, each under
the top-level `file_roots/_hubble`.

.. code-block:: diff

     salt
     └── _beacons
     └── _modules
     └── _grains
     └── _renderers
     └── _returners
     └── _states
     └── _output
     └── _utils
   + └── _hubble
   +     ├── nebula
   +     ├── nova
   +     ├── pulsar
   +     └── quasar

