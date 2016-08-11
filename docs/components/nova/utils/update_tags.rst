utils/update_tags.py
~~~~~~~~~~~~~~~~~~~~

This script does four things:

 #. Updates tags in yaml profile to match the cis standards, saved at <yaml>_updated.yaml.
 #. Finds format errors in yaml profile.
 #. Finds outdated audits in the yaml profile.
 #. Finds audits in the cis standards that aren't found in the yaml profile.

It also saves a log of the results of each run at <.yaml>_updated.log

Optional tags:
  -t : templates cis standards that aren't included in yaml into the updated version.

.. code-block:: shell

    python ./update_tags.py <optional_tag> <profile.yaml> <profile.xls>
