openssl
-------

==========  ======================
maintainer  HubbleStack / avb76
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`, python-OpenSSL
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/openssl.py
==========  ======================

.. _SaltStack: https://saltstack.com

HubbleStack Nova module for auditing SSL certificates.

Configuration
~~~~~~~~~~~~~

Sample YAML data, with in line comments:

.. code-block:: yaml
   :linenos:


    openssl:                                # module definition
      google:                               # unique ID
        data:                               # required key
          tag: 'CERT-001'                   # TAG
          endpoint: 'www.google.com'        # https endpoint
          file: False                       # PEM input file
          port: 443                         # port (default: 443)
          not_after: 15                     # optional
          not_before: 2                     # optional
          fail_if_not_before: False         # optional
        description: 'google certificate'

Some words about the elements in the data dictionary:
 * ``tag``: this check's unique TAG
 * ``endpoint``: the ssl endpoint to check (``endpoint`` or ``file``)
 * ``file``: the path to the ``.pem`` file containing the SSL certificate to be checked
 * ``port``: (optional) defaults to 443
 * ``not_after``: the minimum number of days left until the certificate should expire
 * ``not_before``: the expected number of days until the certificate becomes valid
 * ``fail_if_not_before``:  if ``True``, the check will fail only if ``not_before`` is ``0`` (or missing)

Known issues
~~~~~~~~~~~~ 

For unknown reasons (yet), the module can fail downloading the certificate from
certain endpoints. When this happens, the check will fail.
