netstat
-------

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/modules/netstat.py
==========  ====================

.. _SaltStack: https://saltstack.com

HubbleStack Nova module for auditing open ports.

Configuration
~~~~~~~~~~~~~

Sample data for the netstat whitelist:

.. code-block:: yaml
   :linenos:


    netstat:                  # module definition
        ssh:                  # unique id
            address: '*:22'   # netstat output match
        another_identifier:   # unique id
            address:          # multiline output match
              - 127.0.0.1:80  # multiline output match
              - 0.0.0.0:80    # multiline output match
