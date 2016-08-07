command
-------

:maintainer: HubbleStack / basepi
:maturity: 2016.7.0
:platform: All
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/command.py

This module is designed to catch those one-off, more complex audits that are
not covered by the other modules. Most of the other modules are far less
complex in their syntax and generally cover 99% of the use-cases.

Here we have an example of the ``command`` module YAML syntax:

**command**

.. code-block:: yaml
   :linenos:


    command:
      nodev_mount:
        data:
          'Centos Linux-7':
            - "grep '[[:space:]]/home[[:space:]]' /etc/fstab":
                match_output: nodev
                match_output_regex: False

**definition**:

 #. ``command``: module definition (required)
 #. ``nodev_mount``: globally unique audit id
 #. ``data``: (required)
 #. ``CentOS Linux-7``: minion 'osfinger' grain value
 #. ``"grep '[[:space:]]/home[[:space:]]" /etc/fstab"``: any valid shell syntax
 #. ``match_output: nodev``: find ``nodev`` in output
 #. ``match_output_regex: False``: use regex when matching (default: False)
