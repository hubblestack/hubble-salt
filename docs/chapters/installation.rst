Getting started with Hubble
===========================

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

 * *Nova* - Nova is Hubble's profile-based auditing engine.
 * *Pulsar* - Pulsar is Hubble's real-time event notification system.
 * *Nebula* - Nebula is Hubble's compliance snapshot utility.
 * *Quasar* - Quasar is Hubble's flexible reporting suite.

Each of the above components are modular, flexible, and easy to drop into
place for any size infrastructure. Pre-built profiles, snapshot templates and
report dashboards are included in the repository.

Hubble - Installation
---------------------

1. Clone the HubbleStack Nova repository and copy `_modules/hubble.py` into
   `salt/_modules`.

.. code-block:: shell

    $ git clone https://github.com/HubbleStack/Nova.git hubblestack-nova.git
    $ cp hubblestack-nova.git/_modules /srv/salt/
    $ cp hubblestack-nova.git/hubblestack_nova /srv/salt/


2. Sync the new module out to each Salt minion:

.. code-block:: shell

    $ salt \* saltutil.sync_modules

Hubble - Usage
--------------

Hubble provides pre-built profiles based on defined standards such as CIS, DISA STIG
and more. These profiles simply need to be defined in a map-like "top file".
This allows for very granular targeting of profiles to any grouping of systems.
Below are a couple examples of these auditing maps:

.. code-block:: yaml

    nova:
      '*':
        - cve_scan
        - CIS-CentOS-7-L1-scored
      'web*':
        - firewall
        - CIS-CentOS-7-L2-scored
        - CIS-CentOS-7-apache24-L1-scored
      'G@os_family:debian':
        - netstat
        - CIS-Debian-7-L2-scored: 'CIS*'
        - CIS-Debian-7-mysql57-L1-scored: 'CIS 2.1.2'


Hubble Functions
----------------

Hubble's core module supports a couple of functions used in distributing,
loading and running these audits. These three functions are: `sync`, `load`,
and `audit`. Examples of running each is described below:

**hubble.sync**

This function will ensure that your `hubblestack_nova` directory and contents
are synced to the targeted minions.

.. code-block:: shell

    $ salt \* hubble.sync

**hubble.load**

This function will load the synced modules distributed using `hubble.sync`.
This can be used to ensure the expected module is loaded and compatible with
the platform.

.. code-block:: shell

    $ salt \* hubble.load

**hubble.audit**

Finally you can run `hubble.audit` to audit your systems.

.. code-block:: shell

    $ salt \* hubble.audit

.. note::

    By default the hubble.audit function will sync and load the
    modules automatically.
