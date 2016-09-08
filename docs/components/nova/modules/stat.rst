stat
----

==========  ====================
maintainer  HubbleStack / avb76
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/stat.py
==========  ====================

.. _SaltStack: https:/saltstack.com

HubbleStack Nova module for using stat to verify ownership & permissions.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

.. code-block:: yaml
   :linenos:


    stat:                                             # module definition
      grub_conf_owner:                                # unique ID
        data:                                         # required key
          'CentOS-6':                                 # osfinger grain
            - '/etc/grub.conf':                       # path to configuration file
                tag: 'CIS-1.5.1'                      # TAG
                user: 'root'                          # expected user
                uid: 0                                # expected uid 
                group: 'root'                         # expected group
                gid: 0                                # expected gid
        description: 'Grub must be owned by root'     # description of audit

          'CentOS Linux-7':                           # osfinger grain
            - '/etc/grub2/grub.cfg':                  # path to configuration file
                tag: 'CIS-1.5.1'                      # TAG
                user: 'root'                          # expected user
                uid: 0                                # expected uid
                group: 'root'                         # expected group
                gid: 0                                # expected gid
        description: 'Grub must be owned by root'     # description of audit
