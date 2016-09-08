vulners.com (cve.scan-v2-salt example)
--------------------------------------

This example pulls from the ``salt://`` fileserver.

.. literalinclude:: ../../../nova/hubblestack_nova_profiles/cve/scan-v2-salt.yaml
   :language: yaml
   :emphasize-lines: 3
   :linenos:

.. seealso:: :doc:`Nova utility - utils/cve_store<../utils/cve_store>`

YAML
~~~~

 #. ``ttl`` - how long, in seconds, should we cache the CVE data. (default: 24hrs)
 #. ``url`` - an ``http://``, ``https://`` or ``salt://`` URL where the required CVE data can be found.
 #. ``control`` - (optional) limit the CVE score reported as ``Failure``.
 #. ``score`` - (optional) severity score between 1-10.

.. tip:: When the url is NOT ``vulners.com``, this module will simply fetch the
         URI defined. No auto-detection is done.

If you need to support multiple distributions you'll need to create a unique
profile for each distribution and target accordingly in the ``top.nova``.
