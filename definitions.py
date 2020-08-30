import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")

RIVM_BASE_URL = 'https://data.rivm.nl/covid-19/'

BASIC_NATIONAL_DATA_FILENAME = "cases_NL.csv"

RIVM_FILES = {
    "COVID-19_casus_landelijk.csv": BASIC_NATIONAL_DATA_FILENAME,
    "COVID-19_aantallen_gemeente_cumulatief.csv": "cases_regional.csv",
}

DAILY_CASES_FILENAME = "cases_daily.csv"
