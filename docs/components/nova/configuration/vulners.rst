vulners.com
-----------

:maintainer: HubbleStack / jaredhanson11
:maturity: 2016.7.0
:platform: Unix
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/cve_scan_v2.py

HubbleStack Nova module for auditing installed packages. Uses https://vulners.com database.

A vulners.com profile looks like the example below:

.. code-block:: yaml

    cve_scan_v2:
      ttl: 86400
      url: https://vulners.com
      #control:
      #  score: 4

The first three lines are required while the fourth and fifth are optional.

 #. ``cve_scan_v2`` - module definition
 #. ``ttl`` - time-to-live (ttl) in seconds to cache JSON data
 #. ``url`` - http(s) or salt:// endpoint for JSON data
