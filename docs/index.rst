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

While each of these components can be used standalone it is often required
to combine each components with it's corresponding Quasar module. Quasar
modules are what connects Nova, Nebula and Pulsar to external endpoints such as
Splunk, Slack, etc.

----------

New to HubbleStack? Explore some of these topics:

Nova
~~~~

Nova is the best place to get started with Hubble. Using pre-built security and
compliance "profiles", Nova will give you a complete picture of your security
stance.

Check out the installation docs:

 * :ref:`Package Installation <nova_installation_packages>` (stable)
 * :ref:`Manual Installation <nova_installation_manual>` (develop)

Have a look at the Nova module list, and learn how audit modules work.

 * :doc:`Nova Modules<components/nova/modules/index>`

... or read through some of the pre-built profiles:

 * :doc:`Nova Profiles<components/nova/profiles/index>`

.. tip:: Once you have Nova installed, check out :doc:`Quasar<quasar/README>` next.

----------

Nebula
~~~~~~

.. seealso:: Nebula has a hard dependency on ``osquery``. See install requirements here https://osquery.io/downloads/

Nebula allows you to take snapshots of your systems by scheduling specific
queries. These queries capture information such as:

 * running processes
 * established outbound connections
 * listening processes
 * suid binaries
 * crontab
 * installed packages
 * ...anything else you'd like to query

Check out the installation docs:

 * :ref:`Package Installation <nebula_installation_packages>` (stable)
 * :ref:`Manual Installation <nebula_installation_manual>` (develop)

Have a look at the Nebula modules:

 * :doc:`Nebula Modules<components/nebula/modules/index>`.


.. tip:: Once you have Nebula installed, checkout :doc:`Quasar<quasar/README>` next.

----------

Pulsar
~~~~~~

.. seealso:: Pulsar has a dependency on the Python ``pyinotify`` library. See: :ref:`Pulsar Required Packages <pulsar_installation_required_packages>`

Pulsar watches for filesystem events as they happen and notify you in real-time
regarding any changes.

 * :ref:`Package Installation <pulsar_installation_packages>` (stable)
 * :ref:`Manual Installation <pulsar_installation_manual>` (develop)

You can also take a look at the Pulsar module list:

 * :doc:`Pulsar Modules<components/pulsar/modules/index>`

.. tip:: Next step? Check out the :doc:`Quasar<quasar/README>` modules to collect Pulsar event data.

----------

Quasar
~~~~~~

Quasar modules are integral in collecting and tracking your security data. In
general you'll want to combine each HubbleStack component (Nova, Pulsar,
Nebula) with it's corresponding Quasar module.

 * :ref:`Package Installation <quasar_installation_packages>` (stable)
 * :ref:`Manual Installation <quasar_installation_manual>` (develop)

You can also take a look at the Pulsar module list:

 * :doc:`Quasar Modules<components/quasar/modules/index>`

----------

.. toctree::
   :maxdepth: 1

   components/index
