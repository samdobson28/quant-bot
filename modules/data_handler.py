# data_handler.py

import pandas as pd
import datetime
from modules.query_alpaca_api import query_alpaca_api_v1beta3

def get_crypto_historic_bars_v1beta3(
    symbols: list, 
    timeframe: str, 
    limit: int, 
    start_date: datetime.datetime, 
    end_date: datetime.datetime
) -> pd.DataFrame:
    """
    Function to retrieve historical cryptocurrency candlestick data from Alpaca (v1beta3).
    """
    if not isinstance(start_date, datetime.datetime) or not isinstance(end_date, datetime.datetime):
        raise ValueError("Start and end dates must be datetime objects.")

    if start_date > end_date:
        raise ValueError("Start date cannot be after end date.")

    symbols_joined = ",".join(symbols)
    start_date_str = start_date.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_date_str = end_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    params = {
        "symbols": symbols_joined,
        "timeframe": timeframe,
        "limit": limit,
        "start": start_date_str,
        "end": end_date_str,
        "sort": "asc",
    }

    url = "https://data.alpaca.markets/v1beta3/crypto/us/bars"

    try:
        json_response = query_alpaca_api_v1beta3(url, params)
    except Exception as e:
        print(f"Error fetching crypto data: {e}")
        raise

    if "bars" not in json_response:
        print(f"Unexpected response: {json_response}")
        return pd.DataFrame()

    # Process the response
    bars_df = pd.DataFrame()
    for symbol in symbols:
        symbol_bars = json_response.get("bars", {}).get(symbol, [])
        if not symbol_bars:
            continue

        symbol_bars_df = pd.DataFrame(symbol_bars)
        symbol_bars_df["symbol"] = symbol

        symbol_bars_df = symbol_bars_df.rename(
            columns={
                "o": "candle_open",
                "h": "candle_high",
                "l": "candle_low",
                "c": "candle_close",
                "v": "candle_volume",
                "t": "candle_timestamp",
                "vw": "vwap",
            }
        )

        bars_df = pd.concat([bars_df, symbol_bars_df], ignore_index=True)

    return bars_df
