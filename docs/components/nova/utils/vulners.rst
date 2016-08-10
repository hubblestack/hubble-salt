vulners.com
~~~~~~~~~~~

A script that will query vulners.com/api for cve data related to given
operating systems.  The data is returned in a valid json format for use in the
cve_scan_v2 module. The json file is stored at the local directory under
<os_name>_<version>.json. Inputs must be in the form os-version, like
'centos-7' or 'ubuntu-16.04' etc.

.. code-block:: shell

    python ./cve_store.py (<os-version>) [<os-version> ...]
