utils/cve_store.py
------------------

==========  =========
maintainer  HubbleStack / jaredhanson11
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/utils/cve_store.py
==========  =========

.. _SaltStack: https://saltstack.com

This python script will query the https://vulners.com API for the required CVE
data related to the given operating system. Data is returned in a valid JSON
format, which can be served via ``salt://``.

Usage
~~~~~

The ``cve_store.py`` utility takes a space-delimited list of ``distro-version``:

.. code-block:: shell

    python ./cve_store.py centos-7 ubuntu-16.04 debian-8

The JSON files will be downloaded and stored in the current working directory
using the naming syntax: ``<distro>_<version>.json>``.

Once you've downloaded the files you need you'll need to update or create new
profiles that will use the downloaded data.

.. seealso:: :doc:`vulners.com (cve.scan-v2-salt) profile <../profiles/vulners-salt>`
