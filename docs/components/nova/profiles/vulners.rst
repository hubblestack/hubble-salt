vulners.com (cve.scan-v2 example)
---------------------------------

This example pulls directly from vulners.com:

.. literalinclude:: ../../../nova/hubblestack_nova/cve/scan-v2.yaml
   :language: yaml
   :emphasize-lines: 3
   :linenos:

.. tip:: When the url is ``vulners.com``, this module will automatically
         determine the distribution and version and query the API accordingly.

YAML
~~~~

 #. ``ttl`` - how long, in seconds, should we cache the CVE data. (default: 24hrs)
 #. ``url`` - an ``http://``, ``https://`` or ``salt://`` URL where the required CVE data can be found.
 #. ``control`` - (optional) limit the CVE score reported as ``Failure``.
 #. ``score`` - (optional) severity score between 1-10.
