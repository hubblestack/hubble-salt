CVE Scanning
============

Another major component of the Nova auditing system is the on-demand CVE
scanning and reporting. This component automates the ingestion of security
advisory announcements, along with parsing, scanning and reporting. This
feature was inspired by FreeBSD's VuXML integration with `pkg audit`.

To run an on-demand CVE scan, ensure that the `oscap` execution module is
synced to your systems along with a security advisory XML feed. (Current
support for this is limited to RHEL. CentOS planned immediately after).

Red Hat publishes security advisories in the form of an XML file. These files
follow a specific standard, which requires an additional dependency to use:
openscap-scanner (http://open-scap.org).

The XML files can be found here: https://www.redhat.com/security/data/oval/.

Simply install the required package, place the XML in your state tree and you
should then be able to scan your system for vulnerabilities.

.. code-block:: shell

    [root@ip-172-31-36-98 ~]# salt \* oscap.scan salt://com.redhat.rhsa-RHEL7.xml
        rhel-7-aws-4:
            ----------
            Total:
                23
            Vulnerabilities:
                - RHSA-20160685 : https://rhn.redhat.com/errata/RHSA-2016-0685.html
                - RHSA-20160534 : https://rhn.redhat.com/errata/RHSA-2016-0534.html
                - RHSA-20160532 : https://rhn.redhat.com/errata/RHSA-2016-0532.html
                - RHSA-20160465 : https://rhn.redhat.com/errata/RHSA-2016-0465.html
                - RHSA-20160459 : https://rhn.redhat.com/errata/RHSA-2016-0459.html
                - RHSA-20160428 : https://rhn.redhat.com/errata/RHSA-2016-0428.html
                - RHSA-20160370 : https://rhn.redhat.com/errata/RHSA-2016-0370.html
                - RHSA-20160301 : https://rhn.redhat.com/errata/RHSA-2016-0301.html
                - RHSA-20160189 : https://rhn.redhat.com/errata/RHSA-2016-0189.html
                - RHSA-20160185 : https://rhn.redhat.com/errata/RHSA-2016-0185.html
                - RHSA-20160176 : https://rhn.redhat.com/errata/RHSA-2016-0176.html
                - RHSA-20160073 : https://rhn.redhat.com/errata/RHSA-2016-0073.html
                ...[snip]...

In the future we plan to expand this report to include enough data to populate
end-user dashboards for reporting, etc.

To include a CVE scan in your Nova top file, simply add the name of the XML
feed into a new Nova profile, like this:

.. code-block:: yaml

    cve_scan: salt://com.redhat.rhsa-RHEL7.xml

.. note::

    tl;dr - dash-delimited filenames only

    You may be tempted to name the Nova profile the same name as the XML file.
    Remember, a '.' is a directory-separator in Hubble, meaning you'd actually
    be pointing to a file salt://com/redhat/rhsa-RHEL7/xml.

Next add that new profile to the Nova top file:

.. code-block:: yaml

  nova:
    'rhel-6-aws-*':
      - rhsa-rhel-6
      - cis-rhel-6-l1-scored
    'rhel-7-aws-*':
      - rhsa-rhel-7
      - cis-rhel-7-l1-scored

Finally, `hubble.audit` will read the `top.nova` and apply the listed checks to
the listed hosts.
