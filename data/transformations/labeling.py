# data/transformations/labeling.py

import pandas as pd

def add_future_returns(df: pd.DataFrame, horizon: int = 1) -> pd.DataFrame:
    """
    Adds a 'future_return' column as a potential target for ML.
    horizon=1 means 1 bar (day if '1D' timeframe) ahead.

    future_return = (close[t + horizon] / close[t]) - 1
    """

    df["future_return"] = df.groupby("symbol")["close"].shift(-horizon) / df["close"] - 1
    return df
