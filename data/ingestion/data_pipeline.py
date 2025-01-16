# data/ingestion/data_pipeline.py

import datetime

# Ingestion
from data.ingestion.alpaca_fetcher import fetch_crypto_bars

# Transformations
from data.transformations.cleaning import clean_data
from data.transformations.feature_engineering import add_technical_indicators
from data.transformations.labeling import add_future_returns

# Storage (DB)
from data.storage.db_store import save_to_db

def run_data_pipeline_db(symbols, timeframe, start_date, end_date, table_name="crypto_bars"):
    """
    Orchestrate your data pipeline, saving final data to a PostgreSQL database.
    """

    print("=== [Data Pipeline] Starting pipeline to DB ===")
    
    # 1) Fetch raw data
    print("[1/5] Fetching data...")
    raw_df = fetch_crypto_bars(symbols, timeframe, start_date, end_date)

    if raw_df.empty:
        print("No data returned from the fetch step. Exiting pipeline.")
        return None

    # 2) Clean data
    print("[2/5] Cleaning data...")
    cleaned_df = clean_data(raw_df)

    # 3) Feature engineering
    print("[3/5] Adding technical indicators...")
    fe_df = add_technical_indicators(cleaned_df)

    # 4) Labeling
    print("[4/5] Adding future returns (labels)...")
    labeled_df = add_future_returns(fe_df, horizon=1)

    # 5) Save to the database
    print(f"[5/5] Saving processed data to table '{table_name}' in PostgreSQL...")
    save_to_db(labeled_df, table_name)

    print("=== [Data Pipeline] Complete ===")
    return labeled_df


if __name__ == "__main__":
    symbols = ["BTC/USD"]
    timeframe = "1D"
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 1, 10)

    run_data_pipeline_db(symbols, timeframe, start_date, end_date, table_name="crypto_bars")
