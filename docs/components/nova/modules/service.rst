service
-------

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/service.py
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

    service:
      blacklist:
        telnet:
          data:
            CentOS Linux-6:
              - 'telnet': 'CIS-2.1.1'
            description: 'Telnet is evil'
            alert: email
            trigger: state

**whitelist**:

.. code-block:: yaml

    service:
      whitelist:
        rsh:
          data:
            CentOS Linux-7:
              - 'rsh': 'CIS-2.1.3'
              - 'rsh-server': 'CIS-2.1.4'
          description: 'RSH is awesome'
          alert: email
          trigger: state
