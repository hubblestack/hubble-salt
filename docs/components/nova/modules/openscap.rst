openscap
--------

==========  ==========
maintainer  HubbleStack / cedwards
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`, openscap_, RHEL
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/modules/cve_scan.py
==========  ==========

.. _SaltStack: https://saltstack.com
.. _openscap: https://www.open-scap.org/

This module automates the ingestion of security advisory announcements, CVE
scanning and reporting. This feature was inspired by FreeBSD's VuXML
integration with ``pkg audit``.

To run an on-demand CVE scan, ensure that the ``oscap`` execution module is
synced to your system(s).

Usage
~~~~~

Red Hat publishes security advisories in the form of an XML file. These files
follow a specific standard, which requires an additional dependency to use:
openscap_.

The XML files can be found here: https://www.redhat.com/security/data/oval/.

This module supports fetching CVE data directly from upstream, or serving
locally through your ``salt://`` fileserver.

.. seealso:: :doc:`openscap Profile<../profiles/openscap>`
