import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

RIVM_BASE_URL = 'https://data.rivm.nl/covid-19/'

RIVM_FILES = {
    "COVID-19_casus_landelijk.csv": "cases_NL.csv",
    "COVID-19_aantallen_gemeente_cumulatief.csv": "cases_regional.csv",
}
