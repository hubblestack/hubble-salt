Splunk - Pulsar
---------------

HubbleStack Pulsar-to-Splunk returner

:maintainer: HubbleStack
:maturity: 2016.7.0
:platform: All
:requires: SaltStack

Deliver HubbleStack Pulsar event data into Splunk using the HTTP event
collector. Required config/pillar settings:

.. code-block:: yaml

    hubblestack:
      pulsar:
        returner:
          splunk:
            token: <splunk_http_forwarder_token>
            indexer: <hostname/IP of Splunk indexer>
            sourcetype: <Destination sourcetype for data>
            index: <Destination index for data>
