# data/ingestion/alpaca_fetcher.py

import datetime
import pandas as pd

# You can import your existing function or place the code here directly
# from modules.data_handler import get_crypto_historic_bars_v1beta3
from modules.query_alpaca_api import query_alpaca_api_v1beta3


def fetch_crypto_bars(symbols, timeframe, start_date, end_date, limit=10000):
    """
    Fetch crypto bar data from Alpaca for a list of symbols.
    Returns a single DataFrame containing all requested data.
    """
    if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
        raise ValueError("start_date and end_date must be datetime objects.")

    if start_date > end_date:
        raise ValueError("start_date cannot be after end_date.")

    # Master DataFrame to hold all symbols
    all_bars_df = pd.DataFrame()

    # Fetch each symbol sequentially
    for symbol in symbols:
        bars_df = _get_bars_for_symbol(symbol, timeframe, start_date, end_date, limit)
        if not bars_df.empty:
            all_bars_df = pd.concat([all_bars_df, bars_df], ignore_index=True)

    return all_bars_df


def _get_bars_for_symbol(symbol, timeframe, start_date, end_date, limit):
    """
    Internal helper to fetch bars for a single symbol via query_alpaca_api_v1beta3.
    Replaces your original get_crypto_historic_bars_v1beta3 usage.
    """
    params = {
        "symbols": symbol,
        "timeframe": timeframe,
        "limit": limit,
        "start": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "end": end_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "sort": "asc",
    }

    url = "https://data.alpaca.markets/v1beta3/crypto/us/bars"
    
    try:
        json_response = query_alpaca_api_v1beta3(url, params)
    except Exception as e:
        print(f"Error fetching crypto data for {symbol}: {e}")
        return pd.DataFrame()

    # Check structure
    if "bars" not in json_response:
        print(f"Unexpected JSON structure for {symbol}: {json_response}")
        return pd.DataFrame()

    # Process the returned data
    symbol_bars = json_response.get("bars", {}).get(symbol, [])
    if not symbol_bars:
        return pd.DataFrame()

    # Convert to DataFrame
    df = pd.DataFrame(symbol_bars)

    # Add the symbol column
    df["symbol"] = symbol

    # Rename columns to keep them consistent
    df.rename(
        columns={
            "o": "candle_open",
            "h": "candle_high",
            "l": "candle_low",
            "c": "candle_close",
            "v": "candle_volume",
            "t": "candle_timestamp",
            "vw": "vwap",
        },
        inplace=True,
    )

    return df
