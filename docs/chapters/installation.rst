Installation
============

One of the primary design goals of Hubble is ease of installation. We've
designed Hubble to be compatible with SaltStack and make it as easy as possible
to install. Full installation instructions detailed below.

(Note: HubbleStack plugins may require additional installation instructions.)

Requirements
============

These instructions assume a basic SaltStack installation; master and minion,
communicating. Once you have this running you can install Hubble in three quick
steps.

Installation
============

Hubble is made up of four different core components. Most of these are
installed via Salt's package management system. The only component that needs
to be manually installed is Nova, Hubble compliance auditing system.

**Step 1:**
-----------

Checkout the latest version of Hubble Nova from GitHub:

.. code-block:: shell

    git clone https://github.com/HubbleStack/Nova.git

**Step 2:**
-----------

Copy `_modules/hubble.py` into your SaltStack installation at `salt/_modules/`.


**Step 3:**
-----------

Sync the new module out to your minions:

.. code-block:: shell

    salt \* saltutil.sync_modules

