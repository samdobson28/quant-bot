import alpaca_trade_api as tradeapi
import time
import uuid
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

def generate_order_id():
    """Generate a unique client order ID."""
    return str(uuid.uuid4())

def place_limit_order(symbol, qty, limit_price):
    """
    Place a limit order for crypto.
    """
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side="buy",
            type="limit",
            time_in_force="gtc",
            limit_price=limit_price,
            client_order_id=generate_order_id()
        )
        print("Limit order placed:", order)
        return order
    except Exception as e:
        print("Error placing limit order:", e)
        return None

def place_stop_limit_order(symbol, qty, stop_price, limit_price):
    """
    Place a stop-limit order for crypto to act as a stop-loss.
    """
    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side="sell",
            type="stop_limit",
            time_in_force="gtc",
            stop_price=stop_price,
            limit_price=limit_price
        )
        print("Stop-limit (stop-loss) order placed:", order)
        return order
    except Exception as e:
        print("Error placing stop-limit order:", e)
        return None

def wait_for_order_fill(order_id, timeout=60):
    """
    Wait for the given order to be filled within the timeout period.
    :param order_id: The ID of the order to monitor.
    :param timeout: Maximum time to wait in seconds.
    :return: Filled order or None if not filled within the timeout.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        order = api.get_order(order_id)
        if order.status == "filled":
            print("Order filled:", order)
            return order
        print(f"Waiting for order to fill... Current status: {order.status}")
        time.sleep(5)  # Check every 5 seconds
    print("Order not filled within the timeout period.")
    return None
