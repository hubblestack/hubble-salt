netstat
-------

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/netstat.py
==========  ====================

.. _SaltStack: https://saltstack.com

HubbleStack Nova module for auditing open ports.

Configuration
~~~~~~~~~~~~~

Sample data for the netstat whitelist:

.. code-block:: yaml

    netstat:
        ssh:
            address: '*:22'
        another_identifier:
            address:
              - 127.0.0.1:80
              - 0.0.0.0:80
