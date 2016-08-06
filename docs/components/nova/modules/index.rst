Modules
-------

This directory structure is a collection of platform-compatible audit modules
and YAML-based "profiles". All contents of this directory are synced to
targeted minions using the ``hubble.sync`` command (or automatically synced based
on the ``hubblestack:nova:autosync`` configuration setting). Audits can then be
targeted by module name or "tag".

Profile Compatibility
---------------------

Early on in this project it became obvious that we would need to support
multiple distributions and platforms. Everything from CentOS to Debian, and BSD
to Windows. This section describes how that compatibility is defined and
determined.

__virtual__()
-------------

Each audit module (``.py`` file) includes a ``__virtual__()`` function that
defines the platform(s) the module supports. If you're already familiar with
writing modules for SaltStack, it works the same way. For those unfamiliar,
this function is executed automatically and loaded or ignored based on the
result of this function. Because we leverage SaltStack's module abstraction
layer, most modules are supported on most platforms, but if you're ever unsure
you can check the logic within that function.

YAML profiles
-------------

Most of the included audit modules require defined "profiles", which provide
the information on what exactly should be audited. These "profiles" are written
in YAML syntax and follow a general structure. In this section I'll outline the
basic YAML structure of the core modules, and give examples of adding support
for additional distributions.

The end-goal of this design is that even non-programmers can write and
contribute to audit "profiles", lowering the bar for contribution.

The pkg module example
----------------------

The ``pkg`` module audits based on a whitelist or blacklist of installed
packages. The general YAML syntax looks as follows:

.. code-block:: yaml

    pkg:
      blacklist:

        unique_id:
          data:
            'osfinger':
              - 'pkg_name': 'TAG'
          description: 'reasoning behind whitelist/blacklist'

Given the above example, supporting a distribution or platform within a
"profile" is as simple as adding two lines below the `data` key:

#. ``osfinger`` grain of platform (ie; CentOS Linux-7, Ubuntu-14.04, FreeBSD-10)
#. The package name and corresponding unique TAG for that platform.

If you are unsure the ``osfinger`` grain for your platform, use the following
command:

.. code-block:: shell

    salt \* grains.get osfinger

Generally speaking, the ``osfinger``, ``pkg_name`` and ``TAG`` will be unique
per platform. Because packages don't always share the same naming scheme
between distributions, this will need to be determined on a per-package basis.
Also, the TAG value generally follows a naming pattern based on the standard
that you're auditing against. Examples might be: ``CIS-2.1.1``, ``STIG-X.Y`` or
even ``CUSTOM-N.M``.

If you are contributing checks to this project, it is important to accurately
tie the ``osfinger``, ``pkg_name`` and ``TAG`` to the upstream benchmark that
you're contributing a profile for.

Global Compatibility
--------------------

For those situations where a check may be globally compatible, the ``osfinger``
value can be replaced with a ``*`` glob. The ``*`` glob defines global
compatibility, and will be run on all platforms (assuming the underlying
``__virtual__()`` successfully applies).

Modules
-------

.. toctree::
   :maxdepth: 1

   command
   grep
   iptables
   netstat
   openscap
   openssl
   pkg
   service
   stat
   sysctl
   vulners
