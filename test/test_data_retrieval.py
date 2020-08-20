"""
Test retrieval of files
"""

import os
import sys
print(sys.path)

from src.utils import get_data_path, get_rivm_filenames
from src.ingest.load_data import retrieve_rivm_datasets

def test01_rivm_data_retrieval():

    retrieve_rivm_datasets()

    # data path should exist
    assert(os.path.exists(get_data_path()))

    # data path should contain rivm datasets
    expected_filenames = list(get_rivm_filenames().values())
    assert(all(elem in os.listdir(get_data_path()) for elem in expected_filenames))

