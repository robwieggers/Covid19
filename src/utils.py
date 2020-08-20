from definitions import ROOT_DIR, RAW_DATA_DIR, PROCESSED_DATA_DIR, RIVM_BASE_URL, RIVM_FILES, BASIC_NATIONAL_DATA_FILENAME
from pathlib import Path


def get_root_path() -> Path:
    """
    Return the root of project
    Returns: path of root of project

    """

    return ROOT_DIR


def get_raw_data_path() -> Path:
    """
    Return the data directory within the project
    Returns: path of data directory within the project

    """

    return RAW_DATA_DIR


def get_processed_data_path() -> Path:
    """
    Return the data directory within the project
    Returns: path of data directory within the project

    """

    return PROCESSED_DATA_DIR


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

    return RIVM_FILES


def get_basic_national_data_filename() -> str:
    """
    Returns the filename of the file with national basic data
    Returns:

    """

    return BASIC_NATIONAL_DATA_FILENAME