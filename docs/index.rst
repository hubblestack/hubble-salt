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

.. _Nova:   /nova/README.html
.. _Pulsar: /pulsar/README.html
.. _Nebula: /nebula/README.html
.. _Quasar: /quasar/README.html


Each of these components are modular, flexible, and easy to drop into place for
any size infrastructure. 

----------

New to HubbleStack? Explore some of these topics:

**Nova**

 * `Nova Modules`_
 * `Nova Profiles`_

----------

**Nebula**

 * `Nebula Modules`_
 * `Nebula Configuration`_

----------

**Pulsar**

 * `Pulsar Modules`_
 * `Pulsar Configuration`_

----------

**Quasar**

 * `Quasar Modules`_
 * `Quasar Configuration`_

.. _`Nova Modules`: /components/nova/modules/index.html
.. _`Nova Profiles`: /components/nova/configuration/index.html

.. _`Nebula Modules`: /components/nebula/modules/index.html
.. _`Nebula Configuration`: /components/nebula/configuration/index.html

.. _`Pulsar Modules`: /components/pulsar/modules/index.html
.. _`Pulsar Configuration`: /components/pulsar/configuration/index.html

.. _`Quasar Modules`: /components/quasar/modules/index.html
.. _`Quasar Configuration`: /components/quasar/configuration/index.html

----------

.. toctree::
   :maxdepth: 1

   components/index
