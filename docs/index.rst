HubbleStack: Security for DevOps
================================

Welcome to the HubbleStack documentation!

Hubble is a modular, open-source security compliance framework built on top of
SaltStack. The project provides on-demand profile-based auditing, real-time
security event notifications, automated remediation, alerting and reporting.

Hubble can "dock" with any existing SaltStack installation, and requires very
little work to get started. This document describes installation, configuration
and general use.

Components 
----------

Hubble is made up of four different components, each playing a role in the
overall auditing of your systems. These components are described here:

 * Nova_ - Nova is Hubble's profile-based auditing engine.
 * Pulsar_ - Pulsar is Hubble's real-time event system.
 * Nebula_ - Nebula is Hubble's security snapshot utility.
 * Quasar_ - Quasar is Hubble's flexible reporting suite.

.. _Nova: https://hubblestack.readthedocs.io/en/latest/nova/README.html
.. _Pulsar: https://hubblestack.readthedocs.io/en/latest/pulsar/README.html
.. _Nebula: https://hubblestack.readthedocs.io/en/latest/nebula/README.html
.. _Quasar: https://hubblestack.readthedocs.io/en/latest/quasar/README.html


Each of these components are modular, flexible, and easy to drop into place for
any size infrastructure. 

.. toctree::
   :maxdepth: 1

   components/index
