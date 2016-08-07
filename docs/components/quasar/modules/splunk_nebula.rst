Splunk - Nebula
---------------

HubbleStack Nebula-to-Splunk returner

==========  ===========
maintainer  HubbleStack
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nebula<../../../nebula/README>`
==========  ===========

.. _SaltStack: https://saltstack.com

Deliver HubbleStack Nebula query data into Splunk using the HTTP event
collector. Required config/pillar settings:

Configuration
~~~~~~~~~~~~~

.. code-block:: yaml

    hubblestack:
      nebula:
        returner:
          splunk:
            token: <splunk_http_forwarder_token>
            indexer: <hostname/IP of Splunk indexer>
            sourcetype: <Destination sourcetype for data>
            index: <Destination index for data>
