from modules.executor import (
    check_account,
    fetch_crypto_price,
    place_limit_order,
    place_stop_limit_order,
    wait_for_order_fill
)
from modules.risk_manager import calculate_position_size, validate_trade
from strategies.momentum import calculate_moving_averages, momentum_strategy
import pandas as pd

def main():
    print("Starting Quant Bot...")
    
    # Step 1: Check account status
    account = check_account()
    if account:
        print(f"Account Status: {account['status']}")
        print(f"Equity: {account['equity']}")
        print(f"Buying Power: {account['buying_power']}")
    
    # Step 2: Fetch historical data
    symbol = "BTC/USD"
    historical_data = pd.DataFrame({
        "close": [94000, 94200, 94150, 94300, 94450, 94500, 94700, 94600, 94900, 95100,
                  95250, 95500, 95300, 95400, 95700, 95800, 96000, 95900, 96200, 96100,
                  95000, 94000, 93000, 92000, 91000, 91500, 94000, 96000, 98000, 100000]
    })

    # Step 3: Calculate moving averages
    historical_data = calculate_moving_averages(historical_data)

    # Step 4: Generate trade signal
    signal = momentum_strategy(historical_data, symbol)
    if not signal:
        print("No trade signal generated.")
        return
    
    print(f"Trade signal: {signal['side']} {symbol}")

    # Step 5: Calculate position size
    price = historical_data.iloc[-1]['close']
    equity = float(account["equity"])
    qty = calculate_position_size(symbol_price=price, equity=equity)
    
    # Step 6: Validate trade
    if not validate_trade(symbol, signal["side"], qty, price):
        return
    
    # Step 7: Execute trade
    if signal["side"] == "buy":
        limit_price = price * 1.001  # Slightly above current price
        limit_order = place_limit_order(symbol, qty, limit_price)
        if limit_order:
            # Wait for the limit order to fill
            filled_order = wait_for_order_fill(limit_order.id)
            if filled_order:
                stop_loss_price = float(filled_order.filled_avg_price) * 0.98  # Example: 2% below filled price
                place_stop_limit_order(symbol, qty, stop_loss_price, stop_loss_price * 0.99)

if __name__ == "__main__":
    main()
