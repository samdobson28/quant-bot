def calculate_moving_averages(data, short_window=5, long_window=20):
    """
    Calculate short-term and long-term moving averages.
    """
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()
    print("Moving averages calculated:\n", data.tail())  # Debug
    return data

def momentum_strategy(data, symbol):
    """
    Generate buy or sell signals based on moving average crossover.
    """
    # Ensure we have enough data for both moving averages
    if len(data) < max(data['short_ma'].notnull().idxmax(), data['long_ma'].notnull().idxmax()):
        print("Not enough data for moving averages.")
        return None

    # Debug: Print the last few rows of data
    print("Last 5 rows of data with MAs:\n", data.tail())

    # Check the last two data points for crossover
    prev_row = data.iloc[-2]
    latest_row = data.iloc[-1]

    if prev_row['short_ma'] <= prev_row['long_ma'] and latest_row['short_ma'] > latest_row['long_ma']:
        print("Buy signal generated.")
        return {"symbol": symbol, "side": "buy"}
    elif prev_row['short_ma'] >= prev_row['long_ma'] and latest_row['short_ma'] < latest_row['long_ma']:
        print("Sell signal generated.")
        return {"symbol": symbol, "side": "sell"}

    print("No crossover detected.")
    return None
