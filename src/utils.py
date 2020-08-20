from definitions import ROOT_DIR, DATA_DIR, RIVM_BASE_URL, RIVM_FILES
from pathlib import Path


def get_root_path() -> Path:
    """
    Return the root of project
    Returns: path of root of project

    """

    return ROOT_DIR


def get_data_path() -> Path:
    """
    Return the data directory within the project
    Returns: path of data directory within the project

    """

    return DATA_DIR


def get_rivm_base_url() -> Path:
    """
    Return the base url where RIVM shares data
    Returns: vase url to RIVM data
    """

    return RIVM_BASE_URL


def get_rivm_filenames() -> dict:
    """
    Get a dictionary of RIVM files as keys and local filenames as values
    Returns: dictionary of RIVM filenames

    """