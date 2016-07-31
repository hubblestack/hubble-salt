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

 * **Nova** - Nova is Hubble's profile-based auditing engine.  
 * **Pulsar** - Pulsar is Hubble's real-time event system.  
 * **Nebula** - Nebula is Hubble's security snapshot utility.  
 * **Quasar** - Quasar is Hubble's flexible reporting suite.

Each of these components are modular, flexible, and easy to drop into place for
any size infrastructure. 

Nova - Installation
-------------------

.. toctree::
   :maxdepth: 2

   nova/README

Pulsar - Installation
---------------------

.. toctree::
   :maxdepth: 2

   pulsar/README

Nebula - Installation
---------------------

.. toctree::
   :maxdepth: 2

   nebula/README

Quasar - Installation
---------------------

.. toctree::
   :maxdepth: 2

   quasar/README
