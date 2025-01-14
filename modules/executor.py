import alpaca_trade_api as tradeapi
from config.settings import API_KEY, API_SECRET, ALPACA_BASE_URL

# Initialize Alpaca API client
api = tradeapi.REST(API_KEY, API_SECRET, ALPACA_BASE_URL, api_version='v2')

def check_account():
    """Fetch and display account details."""
    try:
        account = api.get_account()
        print("Account Status:", account.status)
        print("Equity:", account.equity)
        print("Buying Power:", account.buying_power)
    except Exception as e:
        print("Error fetching account details:", e)

def fetch_crypto_price(symbol):
    """Fetch the latest market price of a crypto asset."""
    try:
        barset = api.get_crypto_bars(symbol, '1Min', limit=1).df  # Corrected timeframe
        if not barset.empty:
            latest_bar = barset.iloc[-1]
            print(f"Latest {symbol} Price: {latest_bar['close']}")
        else:
            print(f"No data found for {symbol}")
    except Exception as e:
        print(f"Error fetching price for {symbol}:", e)

if __name__ == "__main__":
    print("Testing Alpaca API integration...")
    check_account()
    fetch_crypto_price("BTC/USD")
