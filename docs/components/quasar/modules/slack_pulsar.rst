Slack - Pulsar
--------------

HubbleStack Pulsar-to-Slack returner.

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Pulsar<../../../pulsar/README>`
==========  ====================

.. _SaltStack: https://saltstack.com

Configuration
~~~~~~~~~~~~~

The following fields can be set in the minion conf or pillar:

.. code-block:: yaml

    slack_pulsar:
      as_user: true            # required for bot profile
      username: calculon       # bot username
      channel: hubble-pulsar   # destination slack channel
      api_key: xoxb-0123456... # unique api key
