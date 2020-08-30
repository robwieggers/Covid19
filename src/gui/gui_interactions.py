"""
Functions interacting with the app
"""

import pandas as pd
import os

from src.utils import get_daily_cases_filename


def load_daily_cases_plot_data(path: str) -> pd.DataFrame:
    """
    Load the file with daily cases data, filter the correct columns and return the dataframe
    Args:
        path: path from which data should be loaded
        layout: common style part of the layout

    Returns: dataframe with data to plot
    """

    try:
        data = list()
        filename = get_daily_cases_filename()
        df = pd.read_csv(os.path.join(path, filename), index_col=0)

        required_columns = [c for c in df.columns if "daily" in c]
        df = df[required_columns]
        df.fillna(0, inplace=True)

        for c in df.columns:
            if c == "cases_daily":
                type = "bar"
                opacity = 0.6
            else:
                type = "lines"
                opacity = 1

            tmp = {
                "x": list(df.index),
                "y": list(df[c]),
                "opacity": opacity,
                "type": type,
                "name": c.split("_")[-2],
                "mode": "lines"
            }
            data.append(tmp)
    except Exception as e:
        print(e)
        data = []

    return data
