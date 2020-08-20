import os

from src.prepare.prepare_national_daily_data import generate_daily_aggregates
from src.utils import get_processed_data_path, get_daily_cases_filename

def test11_test_daily_aggragates():

    generate_daily_aggregates()
    # data path should exist
    assert(os.path.exists(get_processed_data_path()))

    # data path should contain processed data for daily cases
    assert(get_daily_cases_filename() in os.listdir(get_processed_data_path()))
