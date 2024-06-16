# content of test_basic.py

import sys
import os

# Add the formulaone-fe directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'formulaone-fe')))

from formulaone.helpers import get_tidy_data_path
from formulaone.database import initialize_database
from formulaone.core import get_movies_of_year, convert_data_from_table_to_dataframe
from tabulate import tabulate

import pandas as pd


def test_check_dataframe_size():
    df = pd.read_parquet(get_tidy_data_path() / 'current_race.parquet')
    assert df.shape[1] == 26


def test_database_connection():
    dr = initialize_database()
    table_names = dr.tables.all()
    if table_names is not None:
        for t in table_names:
            print(t.name)
        assert True
    else:
        assert False


def test_conversion_of_table_to_dataframe():
    json_movies = get_movies_of_year(2013)
    df = convert_data_from_table_to_dataframe(json_movies)
    print(tabulate(df, headers='keys', tablefmt='psql'))
