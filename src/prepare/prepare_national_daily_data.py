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
from src.utils import get_daily_cases_filename


def generate_daily_aggregates(df_in: pd.DataFrame):
    """
    Generates daily aggregates and stores them

    Generates the daily aggregates of:
    - new cases,
    - delta in hospitalization
    - delta in ICU usage
    and there totals

    Args:
        df_in: raw input data

    """

    df = df_in[["Date_statistics", "Date_file"]].groupby("Date_statistics").count()
    df.columns = ["cases_daily"]

    df["cases_total"] = df["cases_daily"].cumsum()

    for window in [3, 7]:
        df[f"cases_daily_{window}day_mean"] = df["cases_daily"].rolling(window=window, center=True).mean()

    return df


def store_daily_aggregates(df: pd.DataFrame, path: str):
    """

    Args:
        df: dataframe to store
        path: the path to store

    Returns:

    """

    if not os.path.exists(path):
        os.makedirs(path)
    df.to_csv(os.path.join(path, get_daily_cases_filename()))
