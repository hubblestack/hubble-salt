Configuration
-------------

Profile Compatibility
---------------------

The CIS profile example
-----------------------

Global Compatibility
--------------------

For those situations where a check may be globally compatible, the ``osfinger``
value can be replaced with a ``*`` glob. The ``*`` glob defines global
compatibility, and will be run on all platforms (assuming the underlying
``__virtual__()`` successfully applies).

Profiles
--------

.. toctree::
   :maxdepth: 1

   cis
   command
   firewall
   grep
   netstat
   openscap
   openssl
   pkg
   service
   stat
   sysctl
   vulners
