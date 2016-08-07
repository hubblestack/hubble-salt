netstat
-------

:maintainer: HubbleStack / basepi
:maturity: 2016.7.0
:platform: Unix
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/netstat.py

HubbleStack Nova module for auditing listening ports.

Sample profile data for the ``netstat`` module:

**single ip:port**

.. code-block:: yaml

    netstat:
      openssh:
        address: '0.0.0.0:22'

**multiple ip:port**

.. code-block:: yaml
    
    netstat:
      apache:
        address:
          - 0.0.0.0:80
          - 0.0.0.0:443
