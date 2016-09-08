vulners.com
-----------

==========  ==========
maintainer  HubbleStack / jaredhanson11
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/modules/cve_scan_v2.py
==========  ==========

.. _SaltStack: https://saltstack.com

Another major component of the Nova auditing system is the on-demand CVE
scanning and reporting. This component automates the ingestion of security
advisory announcements, and compares this data to the installed packages. This
feature was inspired by FreeBSD's VuXML integration with ``pkg audit``.

This module, ``scan-v2``, uses a public vulnerability database at
https://vulners.com. 

Queries to https://vulners.com are made either directly from the minion or
served from your ``salt://`` fileserver. The defined ``ttl`` in either case
will determine the amount of time the JSON data is cached on the minion.
Example profiles for each of these are found at ``cve.scan-v2`` and
``cve.scan-v2-salt`` respectively.

Configuration
~~~~~~~~~~~~~

The required JSON files can be downloaded using the ``utils/cve_store.py`` tool
found in the Nova repository. These downloaded files can then be served using
``salt://``.

.. seealso:: :doc:`utils/cve_store.py<../utils/cve_store>`

Usage
~~~~~

.. code-block:: shell

    salt \* hubble.audit cve.scan-v2

.. seealso:: :doc:`cve.scan-v2 profile<../profiles/vulners>`

.. code-block:: shell

    salt \* hubble.audit cve.scan-v2-salt

.. seealso:: :doc:`cve.scan-v2-salt profile<../profiles/vulners-salt>`
