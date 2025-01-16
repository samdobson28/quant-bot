# data/tests/test_pipeline_db.py

import pytest
import datetime
from data.ingestion.data_pipeline import run_data_pipeline_db
from data.storage.db_store import load_from_db

@pytest.mark.parametrize("symbols, timeframe, start_date, end_date", [
    (["BTC/USD"], "1D", datetime.datetime(2023, 1, 1), datetime.datetime(2023, 1, 3))
])
def test_run_data_pipeline_db(symbols, timeframe, start_date, end_date):
    """
    Runs the pipeline that saves to PostgreSQL, then checks the data in the DB.
    """
    table_name = "test_crypto_bars_db"  # use a test table

    # Clear or drop the table if it exists, optionally
    # ... (if you want a clean slate each time)

    df = run_data_pipeline_db(symbols, timeframe, start_date, end_date, table_name=table_name)

    # Ensure the pipeline returned a DataFrame
    assert df is not None, "Pipeline returned None."
    assert not df.empty, "DataFrame from pipeline is empty."

    # Now check the data in the DB
    loaded_df = load_from_db(table_name)
    assert not loaded_df.empty, "No rows in DB after pipeline."

    # Check for columns we expect
    expected_cols = {"symbol", "timestamp", "open", "close", "future_return"}
    for col in expected_cols:
        assert col in loaded_df.columns, f"Missing expected column {col}."

    print("test_pipeline_db.py: DB pipeline test passed successfully!")
