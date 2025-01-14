from modules.executor import check_account, fetch_crypto_price, place_order

def main():
    print("Starting Quant Bot...")
    
    # Step 1: Check account status
    account = check_account()
    if account:
        print(f"Account Status: {account['status']}")
        print(f"Equity: {account['equity']}")
        print(f"Buying Power: {account['buying_power']}")
    
    # Step 2: Fetch crypto price
    price = fetch_crypto_price("BTC/USD")
    if price:
        print(f"Latest BTC/USD Price: {price}")
    
    # Step 3: Place a test order
    order = place_order("BTC/USD", qty=0.001, side="buy")
    if order:
        print(f"Final Order Details: {order}")

if __name__ == "__main__":
    main()
