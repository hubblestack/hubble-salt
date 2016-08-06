sysctl
------

:maintainer: HubbleStack / avb76
:maturity: 2016.7.0
:platform: Linux
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/sysctl.py

HubbleStack Nova module for using sysctl to verify sysctl parameter.

This audit module requires yaml data to execute. It will search the local
directory for any .yaml files, and if it finds a top-level 'sysctl' key, it
will use that data.

Sample YAML data, with inline comments:

.. code-block:: yaml

    sysctl:
      randomize_va_space:  # unique ID
        data:
          'CentOS-6':  #osfinger grain
            - 'kernel.randomize_va_space':  #sysctl param to check
                tag: 'CIS-1.6.3'  #audit tag
                match_output: '2'   #expected value of the checked parameter
          'CentOS-7':
            - 'kernel.randomize_va_space':
                tag: 'CIS-1.6.2'
                match_output: '2'
        description: 'Enable Randomized Virtual Memory Region Placement (Scored)'
        alert: email
        trigger: state
