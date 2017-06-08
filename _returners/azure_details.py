'''
HubbleStack Azure Details

:maintainer: HubbleStack
:platform: All
:requires: SaltStack
'''

import requests


def get_azure_details():
    # Gather azure information if present
    azure = {}
    azure['azure_vmId'] = None

    azureHeader = {'Metadata': 'true'}

    try:
        r = requests.get('http://169.254.169.254/metadata/instance/compute/vmId?api-version=2017-03-01&format=text',
                         timeout=1, headers=azureHeader)
        r.raise_for_status()
        azure['azure_vmId'] = r.text
    except (requests.exceptions.RequestException, ValueError):
        # Not on an Azure box
        azure['azure_vmId'] = None
    return azure
