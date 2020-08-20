"""
This module loads data from various data sources

@author: Rob Wieggers
"""

import os
import urllib.request

from src.utils import get_data_path, get_rivm_base_url, get_rivm_filenames


def retrieve_rivm_datasets():
    """
    Retrieve different daily update rivm datasets and store them in ./data

    """

    files_to_retrieve = get_rivm_filenames()

    data_path = get_data_path()
    if not os.path.exists(data_path):
        os.makedirs(get_data_path())

    for remote_filename, local_filename in files_to_retrieve.items():
        remote_path = os.path.join(get_rivm_base_url(), remote_filename)
        local_path = os.path.join(data_path, local_filename)

        urllib.request.urlretrieve(remote_path, local_path)




