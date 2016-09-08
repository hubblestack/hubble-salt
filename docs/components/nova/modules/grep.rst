grep
----

==========  ====================
maintainer  HubbleStack / basepi
maturity    2016.7.0
platform    All
requires    SaltStack_, :doc:`HubbleStack Nova<../../../nova/README>`
source      https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova_modules/modules/grep.py
==========  ====================

.. _SaltStack: https://saltstack.com

HubbleStack Nova plugin for using ``grep`` to verify settings in files.

Supports both blacklisting and whitelisting patterns. Blacklisted patterns must
**not** be found in the specified file. Whitelisted patterns **must** be found in the
specified file.

Configuration
~~~~~~~~~~~~~

Sample profile data, with inline comments:

.. code-block:: yaml
   :linenos:


    grep:                                      # module definition
      whitelist:                               # 'whitelist' or 'blacklist'
        fstab_tmp_partition:                   # unique ID
          data:                                # required key
            CentOS Linux-6:                    # osfinger grain
              - '/etc/fstab':                  # full path to file
                  tag: 'CIS-1.1.1'             # audit tag
                  pattern: '/tmp'              # grep pattern
                  match_output: 'nodev'        # string to check for in output of grep command (optional)
                  match_output_regex: True     # whether to use regex when matching output (default: False)
                  grep_args:                   # extra args to grep
                    - '-E'                     # -E, --extended-regexp
                    - '-i'                     # -i, --ignore-case
                    - '-B2'                    # -B num, --before-context=num
                  match_on_file_missing: True  # See below

            '*':                               # wildcard, will be run if no direct osfinger match
              - '/etc/fstab':                  # full path to file
                  tag: 'CIS-1.1.1'             # audit tag
                  pattern: '/tmp'              # grep pattern

          ## optional
          description: |
            The /tmp directory is intended to be world-writable, which presents a risk
            of resource exhaustion if it is not bound to a separate partition.

If ``match_on_file_missing`` is ommitted, success/failure will be determined
entirely based on the grep command and other arguments. If it's set to ``True``
and the file is missing, then it will be considered a match (success for
whitelist, failure for blacklist). If it's set to ``False`` and the file is
missing, then it will be considered a non-match (success for blacklist, failure
for whitelist).  If the file exists, this setting is ignored.
