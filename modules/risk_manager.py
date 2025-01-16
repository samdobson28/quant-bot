# risk_manager.py

from modules.executor import check_account

def calculate_position_size(symbol_price, equity, risk_percentage=0.02):
    """Calculate position size based on risk percentage."""
    max_risk = equity * risk_percentage
    qty = max_risk / symbol_price
    return round(qty, 6)  # Round to six decimal places for crypto

def validate_trade(symbol, side, qty, symbol_price, max_exposure=0.1):
    """
    Validate trade based on risk limits.
    - Max exposure: Percentage of total equity that can be in the market.
    """
    account = check_account()
    if not account:
        print("Unable to fetch account details for risk management.")
        return False

    total_equity = float(account["equity"])
    current_exposure = (symbol_price * qty) / total_equity

    if current_exposure > max_exposure:
        print(f"Trade rejected: Exceeds max exposure limit of {max_exposure * 100}%")
        return False

    print(f"Trade approved: {side} {qty} of {symbol}")
    return True
