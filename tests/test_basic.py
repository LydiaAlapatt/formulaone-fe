# content of test_sample.py

from formulaone.helpers import get_tidy_data_path
from formulaone.database import initialize_database
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
