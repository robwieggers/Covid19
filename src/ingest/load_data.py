"""
This module loads data from various data sources

@author: Rob Wieggers
"""

import os
import urllib.request

from src.utils import get_raw_data_path, get_rivm_base_url, get_rivm_filenames


def retrieve_rivm_datasets(data_path):
    """
    Retrieve different daily update rivm datasets and store them in ./data

    Args:
        data_path: source path of the rivm datasets

    """

    files_to_retrieve = get_rivm_filenames()

    if not os.path.exists(data_path):
        os.makedirs(get_raw_data_path())

    for remote_filename, local_filename in files_to_retrieve.items():
        remote_path = os.path.join(get_rivm_base_url(), remote_filename)
        local_path = os.path.join(data_path, local_filename)

        urllib.request.urlretrieve(remote_path, local_path)
