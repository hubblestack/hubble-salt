Splunk - Nova
-------------

HubbleStack Nova-to-Splunk returner

==========  ===========
maintainer  HubbleStack
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
==========  ===========

.. _SaltStack: https://saltstack.com

Deliver HubbleStack Nova result data into Splunk using the HTTP event
collector. Required config/pillar settings:

Configuration
~~~~~~~~~~~~~

.. code-block:: yaml

    hubblestack:
      nova:
        returner:
          splunk:
            token: <splunk_http_forwarder_token>
            indexer: <hostname/IP of Splunk indexer>
            sourcetype: <Destination sourcetype for data>
            index: <Destination index for data>
