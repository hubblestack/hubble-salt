openscap (cve.scan-v1 example)
------------------------------

Red Hat publishes security advisories in the form of an XML file. These files
follow a specific standard (OVAL) which requires an additional dependency to
use. This profiles underlying module relies on ``openscap-scanner``
(https://www.open-scap.org).

The XML files can be found here: https://www.redhat.com/security/data/oval/.

Simply point to your preferred OVAL file:

Upstream
~~~~~~~~

.. literalinclude:: ../../../nova/hubblestack_nova/cve/scan-v1.yaml
   :language: yaml
   :linenos:

salt://
~~~~~~~

To include a CVE scan in your Nova top file, simply add the name of the XML
feed into a new Nova profile:

.. code-block:: yaml
   :linenos:

    cve_scan: salt://com-redhat-rhsa-RHEL7.xml

.. seealso:: :doc:`openscap Audit Module<../modules/openscap>`

.. tip:: tl;dr - dash-delimited filenames only

    You may be tempted to name the Nova profile the same name as the XML file.
    Remember, a '.' is a directory-separator in Hubble (and Salt), meaning you'd actually
    be pointing to a file salt://com/redhat/rhsa-RHEL7/xml.
