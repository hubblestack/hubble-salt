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
**not** be installed. Whitelisted packages **must** be installed. Also supported
is requiring a specific version or a minimum or maximum version.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

**blacklist**:

.. code-block:: yaml
   :linenos:

    pkg:                                      # module definition
      blacklist:                              # 'whitelist' or 'blacklist'
        rsh:                                  # unique ID
          data:                               # required key
            CentOS Linux-6:                   # osfinger grain
              - 'rsh': 'CIS-2.1.1'            # pkg_name : TAG
            description: 'RSH is evil'        # description of audit

            CentOS Linux-6:                   # osfinger grain
              - 'rsh':                        # dict format allows version definition
                  tag: 'CIS-2.1.3'            # TAG
                  version: '4.3.2'            # version
            description: 'RSH is evil'        # description of audit

            CentOS Linux-6:                   # osfinger grain
              - 'rsh':                        # dict format allows version definition
                  tag: 'CIS-2.1.3'            # TAG
                  version: '>=4.3.2'          # flexible version
            description: 'RSH is evil'        # description of audit

**whitelist**:

.. code-block:: yaml
   :linenos:


    pkg:                                      # module definition
      whitelist:                              # 'whitelist' or 'blacklist'
        rsh:                                  # unique ID
          data:                               # required key
            CentOS Linux-6:                   # osfinger grain
              - 'rsh': 'CIS-2.1.1'            # pkg_name : TAG
            description: 'RSH is awesome'     # description of audit

              - 'rsh':                        # dict format allows version definition
                  tag: 'CIS-2.1.3'            # TAG
                  version: '4.3.2'            # version
            description: 'RSH is awesome'     # description of audit

              - 'rsh':                        # dict format allows version definition
                  tag: 'CIS-2.1.3'            # TAG
                  version: '>=4.3.2'          # flexible version
            description: 'RSH is awesome'     # description of audit
