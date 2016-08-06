stat
----

:maintainer: HubbleStack / avb76
:maturity: 2016.7.0
:platform: Linux
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/stat.py

HubbleStack Nova module for using stat to verify ownership & permissions.

This audit module requires yaml data to execute. It will search the local
directory for any .yaml files, and if it finds a top-level 'stat' key, it will
use that data.

Sample YAML data, with inline comments:

.. code-block:: yaml

    stat:
      grub_conf_own:  # unique ID
        data:
          'CentOS-6':  # osfinger grain
            - '/etc/grub.conf':  # filename
                tag: 'CIS-1.5.1'  #audit tag
                user: 'root'  #expected owner
                uid: 0        #expected uid owner
                group: 'root'  #expected group owner
                gid: 0          #expected gid owner
          'CentOS Linux-7':
            - '/etc/grub2/grub.cfg':
                tag: 'CIS-1.5.1'
                user: 'root'
                uid: 0
                group: 'root'
                gid: 0
        # The rest of these attributes are optional, and currently not used
        description: 'Grub must be owned by root'
        alert: email
        trigger: state
