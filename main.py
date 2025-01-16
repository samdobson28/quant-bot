# main.py

import datetime
from modules.data_handler import get_crypto_historic_bars_v1beta3

def main():
    print("Starting Quant Bot...")

    # Define parameters
    symbols = ["BTC/USD"]
    timeframe = "1D"
    limit = 100
    start_date = datetime.datetime(2025, 1, 1)
    end_date = datetime.datetime(2025, 1, 15)

    print("Fetching historical crypto data...")
    try:
        historical_data = get_crypto_historic_bars_v1beta3(
            symbols=symbols,
            timeframe=timeframe,
            limit=limit,
            start_date=start_date,
            end_date=end_date
        )
        if historical_data.empty:
            print("No data found for the given parameters.")
        else:
            print("Historical data retrieved:")
            print(historical_data)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
