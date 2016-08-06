command
-------

:maintainer: HubbleStack / basepi
:maturity: 2016.7.0
:platform: All
:requires: SaltStack

:source: https://github.com/HubbleStack/Nova/blob/develop/hubblestack_nova/modules/command.py

Hubble Nova plugin for running arbitrary commands and checking the output of
those commands

Sample YAML data, with inline comments:

.. code-block:: yaml

      # Unique ID for this set of audits
      nodev:
        data:
          # 'osfinger' grain, for multiplatform support
          'Red Hat Enterprise Linux Server-6':
            # tag is required
            tag: CIS-1.1.10
            # `commands` is a list of commands with individual flags
            commands:
              # Command to be run
              - 'grep "[[:space:]]/home[[:space:]]" /etc/fstab':
                  # Check the output for this pattern
                  # If match_output not provided, any output will be a match
                  match_output: nodev
                  # Use regex when matching the output (default False)
                  match_output_regex: False
                  # Invert the success criteria. If True, a match will cause failure (default False)
                  fail_if_matched: False
              - 'mount | grep /home':
                  match_output: nodev
                  match_output_regex: False
                  # Match each line of the output against our pattern
                  # Any that don't match will make the audit fail (default False)
                  match_output_by_line: True
              - ?
                  |
                    echo 'this is a multi-line'
                    echo 'bash script'
                    echo 'note the special ? syntax'
                :
                  # Shell through which the script will be run, must be abs path
                  shell: /bin/bash
                  match_output: this
            # Aggregation strategy for multiple commands. Defaults to 'and', other option is 'or'
            aggregation: 'and'
          # Catch-all, if no other osfinger match was found
          '*':
            tag: generic_tag
            commands:
              - 'grep "[[:space:]]/home[[:space:]]" /etc/fstab':
                  match_output: nodev
                  match_output_regex: False
                  fail_if_matched: False
              - 'mount | grep /home':
                  match_output: nodev
                  match_output_regex: False
                  match_output_by_line: True
            aggregation: 'and'
        # Description will be output with the results
        description: '/home should be nodev'
