"""
Test retrieval of files
"""

import os

from src.utils import get_raw_data_path, get_rivm_filenames
from src.ingest.load_data import retrieve_rivm_datasets


def test01_rivm_data_retrieval():

    data_path = get_raw_data_path()
    retrieve_rivm_datasets(data_path)

    # data path should exist

    assert(os.path.exists(get_raw_data_path()))

    # data path should contain rivm datasets
    expected_filenames = list(get_rivm_filenames().values())
    assert(all(elem in os.listdir(get_raw_data_path()) for elem in expected_filenames))
