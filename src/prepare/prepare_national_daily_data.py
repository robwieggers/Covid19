"""
This module prepares the data for the national daily aggregates.
This includes:
- daily new cases
- daily delta in hospitalizations
- daily delta in ICU usage
and the totals for these kpis
"""

import os
import pandas as pd
from src.utils import get_raw_data_path, get_basic_national_data_filename, get_processed_data_path, \
    get_daily_cases_filename


def generate_daily_aggregates():
    """
    Generates daily aggregates and stores them

    Generates the daily aggregates of:
    - new cases,
    - delta in hospitalization
    - delta in ICU usage
    and there totals

    """

    df_raw = pd.read_csv(os.path.join(get_raw_data_path(), get_basic_national_data_filename()), sep=";")
    df = df_raw[["Date_statistics", "Date_file"]].groupby("Date_statistics").count()
    df.columns = ["cases_daily"]

    df["cases_total"] = df["cases_daily"].cumsum()

    for window in [3, 7]:
        df[f"cases_daily_{window}day_mean"] = df["cases_daily"].rolling(window=window, center=True).mean()

    output_directory = get_processed_data_path()
    if not os.path.exists(output_directory):
        os .makedirs(output_directory)
    df.to_csv(os.path.join(output_directory, get_daily_cases_filename()))
