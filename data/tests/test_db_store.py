# data/tests/test_db_store.py

import pytest
import pandas as pd
from data.storage.db_store import save_to_db, load_from_db

@pytest.fixture
def sample_df():
    data = {
        "timestamp": pd.date_range("2023-01-01", periods=3, freq="D"),
        "symbol": ["BTC/USD"] * 3,
        "open": [100, 105, 110],
        "close": [105, 110, 115],
    }
    return pd.DataFrame(data)

def test_save_and_load_db(sample_df):
    table_name = "test_db_store_table"

    # Save
    save_to_db(sample_df, table_name)

    # Load
    loaded_df = load_from_db(table_name)
    assert len(loaded_df) >= 3, "Expected at least 3 rows in DB."

    print("DB store test passed!")
