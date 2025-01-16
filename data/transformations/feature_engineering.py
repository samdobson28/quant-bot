# data/transformations/feature_engineering.py

import pandas as pd

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add one or more technical indicators (e.g., MA, RSI, MACD).
    Demonstrates a simple moving average approach.
    """
    # Simple moving averages
    df["ma_short"] = df.groupby("symbol")["close"].transform(lambda x: x.rolling(window=5).mean())
    df["ma_long"] = df.groupby("symbol")["close"].transform(lambda x: x.rolling(window=20).mean())

    # Example for a daily return column (if you like):
    # df["daily_return"] = df.groupby("symbol")["close"].transform(lambda x: x.pct_change())

    return df
