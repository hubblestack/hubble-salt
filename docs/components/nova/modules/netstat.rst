netstat
-------

:maintainer: HubbleStack / basepi
:maturity: 2016.7.0
:platform: Unix
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/netstat.py

HubbleStack Nova module for auditing open ports.

Sample data for the netstat whitelist:

.. code-block:: yaml

    netstat:
        ssh:
            address: '*:22'
        another_identifier:
            address:
              - 127.0.0.1:80
              - 0.0.0.0:80
