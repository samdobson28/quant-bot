import alpaca_trade_api as tradeapi
from config.settings import API_KEY, API_SECRET, ALPACA_BASE_URL

# Initialize Alpaca API client
api = tradeapi.REST(API_KEY, API_SECRET, ALPACA_BASE_URL, api_version='v2')

def check_account():
    """Fetch and return account details."""
    try:
        account = api.get_account()
        return {
            "status": account.status,
            "equity": account.equity,
            "buying_power": account.buying_power
        }
    except Exception as e:
        print("Error fetching account details:", e)
        return None

def fetch_crypto_price(symbol):
    """Fetch the latest market price of a crypto asset."""
    try:
        barset = api.get_crypto_bars(symbol, '1Min', limit=1).df
        if not barset.empty:
            latest_bar = barset.iloc[-1]
            return latest_bar['close']
        else:
            print(f"No data found for {symbol}")
            return None
    except Exception as e:
        print(f"Error fetching price for {symbol}:", e)
        return None

def place_order(symbol, qty, side):
    """Place a buy or sell order for a crypto asset and monitor its status."""
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type='market',
            time_in_force='gtc'
        )
        print(f"Order placed: {order}")
        
        # Monitor order status
        while order.status not in ["filled", "canceled", "expired"]:
            order = api.get_order(order.id)
            print(f"Order status: {order.status}")
        
        return order
    except Exception as e:
        print(f"Error placing order: {e}")
        return None
