pkg
---

==========  ======================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/pkg.py
==========  ======================

.. _SaltStack: https://saltstack.com

HubbleStack Nova module for auditing installed packages.

Supports both blacklisting and whitelisting pacakges. Blacklisted packages must
not be installed. Whitelisted packages must be installed, with options for
requiring a specific version or a minimum or maximum version.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

**blacklist**:

.. code-block:: yaml

    pkg:
      blacklist: # 'whitelist' or 'blacklist'
        telnet:  # unique ID
          data:  # required key
            CentOS Linux-6: # osfinger grain
              - 'telnet': 'CIS-2.1.1' # pkg_name : TAG
            description: 'Telnet is evil' # description of audit
            alert: False
            trigger: state
              - 'rsh': # dict format allows version definition
                  tag: 'CIS-2.1.3' # TAG
                  version: '4.3.2' # version
            description: 'RSH is awesome'
            alert: # optional
            trigger: # optional

              - 'rsh': # dict format allows version definition
                  tag: 'CIS-2.1.3' # TAG
                  version: '>=4.3.2' # flexible version
            description: 'RSH is awesome'
            alert: # optional
            trigger: # optional

**whitelist**:

.. code-block:: yaml

    pkg:
      whitelist: # 'whitelist' or 'blacklist'
        rsh:     # unique ID
          data:  # required key
            CentOS Linux-6: # osfinger grain
              - 'telnet': 'CIS-2.1.1' # pkg_name : TAG
            description: 'Telnet is the best' # description of audit
            alert: False
            trigger: state
              - 'rsh': # dict format allows version definition
                  tag: 'CIS-2.1.3' # TAG
                  version: '4.3.2' # version
            description: 'RSH is awesome'
            alert: # optional
            trigger: # optional

              - 'rsh': # dict format allows version definition
                  tag: 'CIS-2.1.3' # TAG
                  version: '>=4.3.2' # flexible version
            description: 'RSH is awesome'
            alert: # optional
            trigger: # optional
