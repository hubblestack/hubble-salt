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

 * :doc:`Nova<nova/README>` - Nova is Hubble's profile-based auditing engine.
 * :doc:`Pulsar<pulsar/README>` - Pulsar is Hubble's real-time event system.
 * :doc:`Nebula<nebula/README>`- Nebula is Hubble's security snapshot utility.
 * :doc:`Quasar<quasar/README>` - Quasar is Hubble's flexible reporting suite.

Each of these components are modular, flexible, and easy to drop into place for
any size infrastructure. 

----------

New to HubbleStack? Explore some of these topics:

**Nova**

 * :doc:`Nova Modules<components/nova/modules/index>`
 * :doc:`Nova Profiles<components/nova/configuration/index>`

----------

**Nebula**

 * :doc:`Nebula Modules<components/nebula/modules/index>`
 * :doc:`Nebula Configuration<components/nebula/configuration/index>`

----------

**Pulsar**

 * :doc:`Pulsar Modules<components/pulsar/modules/index>`
 * :doc:`Pulsar Configuration<components/pulsar/configuration/index>`

----------

**Quasar**

 * :doc:`Quasar Modules<components/quasar/modules/index>`
 * :doc:`Quasar Configuration<components/quasar/configuration/index>`

----------

.. toctree::
   :maxdepth: 1

   components/index
