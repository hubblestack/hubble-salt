service
-------

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/modules/service.py
==========  ====================

.. _SaltStack: https://saltstack.com

HubbleStack Nova module for auditing running services.

Supports both blacklisting and whitelisting services. Blacklisted services must
**not** be running. Whitelisted services **must** be running.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

**blacklist**:

.. code-block:: yaml
   :linenos:


    service:                                 # module definiton
      blacklist:                             # 'whitelist' or 'blacklist'
        telnet:                              # unique ID
          data:                              # required key
            CentOS Linux-6:                  # osfinger grain
              - 'telnet': 'CIS-2.1.1'        # pkg_name : TAG
            description: 'Telnet is evil'    # description of audit

**whitelist**:

.. code-block:: yaml
   :linenos:


    service:                                 # module definition
      whitelist:                             # 'whitelist' or 'blacklist'
        rsh:                                 # unique ID
          data:                              # required key
            CentOS Linux-7:                  # osfinger grain
              - 'rsh': 'CIS-2.1.3'           # pkg_name : TAG
              - 'rsh-server': 'CIS-2.1.4'    # pkg_name : TAG
          description: 'RSH is awesome'      # description of audit
