sysctl
------

==========  ====================
maintainer  HubbleStack / avb76
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/sysctl.py
==========  ====================

.. _SaltStack: https:/saltstack.com

HubbleStack Nova module for using sysctl to verify sysctl parameter.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

.. code-block:: yaml
   :linenos:


    sysctl:                                             # module definition
      randomize_va_space:                               # unique ID
        data:                                           # required key
          'CentOS-6':                                   # osfinger grain
            - 'kernel.randomize_va_space':              # sysctl parameter to check
                tag: 'CIS-1.6.3'                        # TAG
                match_output: '2'                       # expected value
        description: 'Enable Randomized Virtual Memory' # description of audit
