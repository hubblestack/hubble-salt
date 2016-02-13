Installation
============

One of the primary design goals of Hubble is ease of installation. We've
designed Hubble, from the start, to be compatible with SaltStack and make it as
easy as possible to install. Full installation instructions detailed below.

(Note: HubbleStack plugins may require additional installation instructions.)

Requirements
============

These instructions assume a basic SaltStack installation; master and minion,
communicating. Once you have this running you can install Hubble in three quick
steps.

Installation
============

**Step 1:**
-----------

Checkout the latest version of Hubble from GitHub:

.. code-block:: shell

    git clone https://github.com/HubbleStack/Hubble.git

**Step 2:**
-----------

Copy `hubble.py` into your SaltStack installation at `salt/_modules/`.


**Step 3:**
-----------

Sync the new module out to your minions:

.. code-block:: shell

    salt \* saltutil.sync_modules




.. toctree::
   :maxdepth: 2

