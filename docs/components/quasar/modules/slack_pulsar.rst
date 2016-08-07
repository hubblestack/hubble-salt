Slack - Pulsar
--------------

HubbleStack Pulsar-to-Slack returner.

:maintainer: HubbleStack
:maturity: 2016.7.0
:platform: All
:requires: SaltStack

Configuration
~~~~~~~~~~~~~

The following fields can be set in the minion conf or pillar:

.. code-block:: yaml

    slack_pulsar.channel (required)
    slack_pulsar.api_key (required)
    slack_pulsar.username (required)
    slack_pulsar.as_user (required to see the profile picture of your bot)
    slack_pulsar.profile (optional)

Slack settings may also be configured as:

.. code-block:: yaml

    slack:
        channel: RoomName
        api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        username: user
        as_user: true

    alternative.slack:
        room_id: RoomName
        api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        from_name: user@email.com

    slack_profile:
        api_key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        from_name: user@email.com

    slack:
        profile: slack_profile
        channel: RoomName

    alternative.slack:
        profile: slack_profile
        channel: RoomName

