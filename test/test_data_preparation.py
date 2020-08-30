import os
import pandas as pd

from src.prepare.prepare_national_daily_data import generate_daily_aggregates, store_daily_aggregates
from src.utils import get_processed_data_path, get_daily_cases_filename, \
    get_raw_data_path, get_basic_national_data_filename
from definitions import TEST_DATA_DIR


def test11_test_generating_and_writing_daily_aggregates():
    """
    Test that data can generated and written

    """

    df_raw = pd.read_csv(os.path.join(TEST_DATA_DIR, get_basic_national_data_filename()), sep=";")
    df = generate_daily_aggregates(df_raw)

    store_daily_aggregates(df, get_processed_data_path())

    # data path should exist
    assert(os.path.exists(get_processed_data_path()))

    # data path should contain processed data for daily cases
    assert(get_daily_cases_filename() in os.listdir(get_processed_data_path()))
