from modules.executor import (
    check_account,
    fetch_crypto_price,
    place_market_order,
    place_stop_limit_order
)
from modules.risk_manager import calculate_position_size, validate_trade

def main():
    print("Starting Quant Bot...")
    
    # Step 1: Check account status
    account = check_account()
    if account:
        print(f"Account Status: {account['status']}")
        print(f"Equity: {account['equity']}")
        print(f"Buying Power: {account['buying_power']}")
    
    # Step 2: Fetch crypto price
    symbol = "BTC/USD"
    price = fetch_crypto_price(symbol)
    if not price:
        return
    
    print(f"Latest {symbol} Price: {price}")
    
    # Step 3: Calculate position size
    equity = float(account["equity"])
    qty = calculate_position_size(symbol_price=price, equity=equity)
    
    # Step 4: Validate trade
    if not validate_trade(symbol, "buy", qty, price):
        return
    
    # Step 5: Place market order
    market_order = place_market_order(symbol, qty)
    if not market_order:
        return
    
    # Step 6: Place stop-limit order as stop-loss
    stop_price = price * 0.98  # Example: 2% below current price
    limit_price = stop_price * 0.99  # Slightly below stop price
    stop_limit_order = place_stop_limit_order(symbol, qty, stop_price, limit_price)
    if stop_limit_order:
        print("Market order and stop-limit (stop-loss) order placed successfully!")

if __name__ == "__main__":
    main()
