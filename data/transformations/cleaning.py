# data/transformations/cleaning.py

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values, duplicates, column renames, data types, etc.
    """

    # Rename columns if needed
    rename_map = {
        "candle_open": "open",
        "candle_high": "high",
        "candle_low": "low",
        "candle_close": "close",
        "candle_volume": "volume",
        "candle_timestamp": "timestamp",
    }
    df = df.rename(columns=rename_map)

    # Convert timestamp to datetime if not already
    if not pd.api.types.is_datetime64_dtype(df["timestamp"]):
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Drop duplicates
    df = df.drop_duplicates(subset=["timestamp", "symbol"])

    # Sort data by time (very important for time-series)
    df = df.sort_values(by=["symbol", "timestamp"]).reset_index(drop=True)

    # Forward-fill or drop rows with NaNs
    # Here, we forward-fill and then drop remaining NaNs if any
    df = df.groupby("symbol").apply(lambda g: g.fillna(method="ffill")).reset_index(drop=True)
    df = df.dropna()

    return df
