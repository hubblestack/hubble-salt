iptables
--------

==========  ===================
maintainer  HubbleStack / avb76
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/firewall.py
==========  ===================

.. _SaltStack: https://saltstack.com

Hubble Nova plugin for using iptables to verify firewall rules.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with inline comments:

.. code-block:: yaml
   :linenos:


    firewall:                                    # module definition
      whitelist:                                 # whitelist or blacklist
        ssh:                                     # unique id
          data:                                  # required key
            tag: 'FIREWALL-TCP-22'               # audit tag
            table: 'filter'                      # table to check (REQUIRED)
            chain: INPUT                         # INPUT / OUTPUT / FORWARD (REQUIRED)
            rule:                                # dict containing the elements for building the rule
              proto: tcp                         # protocol (tcp/udp/icmp)
              dport: 22                          # destination port
              match: state                       # rule match
              connstate: RELATED,ESTABLISHED     # connection state
              jump: ACCEPT                       # 'jump' destination
            family: 'ipv4'                       # iptables family (REQUIRED)
          description: 'ssh iptables rule check' # description of the check

A few words about the auditing logic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The audit function uses the ``iptables.build_rule`` salt execution module to build
the actual iptables rule to be checked.

How are the rules built?
~~~~~~~~~~~~~~~~~~~~~~~~

The elements in the rule dictionary will be used to build the iptables rule.

Note: ``table``, ``chain`` and ``family`` are **not** required under the rule key.
Note: ``iptables.build_rule`` does **not** verify the syntax of the iptables rules.

Here is a list of accepted iptables rules elements, based on the
``iptables.build_rule`` source code:

 * ``command``
 * ``position``
 * ``full``
 * ``target``
 * ``jump``
 * ``proto/protocol``
 * ``if``
 * ``of``
 * ``match``
 * ``match-set``
 * ``connstate``
 * ``dport``
 * ``sport``
 * ``dports``
 * ``sports``
 * ``comment``
 * ``set``
 * ``jump``

Check the following links for more details:
  - `iptables.build_rule`_ - upstream SaltStack documentation
  - `iptables`_ salt execution module source code (search for the ``build_rule`` function inside):

.. _`iptables.build_rule`: https:/docs.saltstack.com/en/latest/ref/modules/all/salt.modules.iptables.html#salt.modules.iptables.build_rule
.. _`iptables`: https:/github.com/saltstack/salt/blob/develop/salt/modules/iptables.py
