
# Quant Bot

## Overview
This repository contains a quant bot for cryptocurrency trading using Alpaca's API. The bot is designed to implement a modular architecture, enabling easy enhancements and robust workflow management. The initial version focuses on executing a momentum-based strategy with built-in risk management.

---

## Current Functionality
### Features
1. **Momentum Strategy**:
   - Implements a moving average crossover strategy to generate buy and sell signals.
   - Uses short-term and long-term moving averages to detect trends.

2. **Order Execution**:
   - Places a **limit order** to buy cryptocurrency when a buy signal is detected.
   - Waits for the limit order to be filled before proceeding.

3. **Risk Management**:
   - Places a **stop-limit order** as a stop-loss mechanism after the limit order is filled.
   - Ensures robust handling of trades to mitigate losses.

4. **Paper Trading**:
   - Fully tested in Alpaca's paper trading environment.

---

## Repository Structure
```
quant-bot/
├── data/
│   ├── raw/                     # Raw data storage (not yet used)
│   ├── processed/               # Processed data storage (not yet used)
│   └── logs/                    # Execution and error logs (future use)
├── strategies/
│   ├── __init__.py              # Strategy package initializer
│   ├── momentum.py              # Momentum strategy implementation
├── modules/
│   ├── data_handler.py          # Placeholder for data fetching and preprocessing
│   ├── executor.py              # Core trading logic (order placement, monitoring)
│   ├── risk_manager.py          # Risk management (position sizing, validation)
│   ├── strategy_loader.py       # Placeholder for loading strategies dynamically
│   └── monitor.py               # Placeholder for trade monitoring and alerts
├── config/
│   ├── settings.py              # Configuration for API keys and Alpaca settings
├── tests/                       # Placeholder for unit and integration tests
├── notebooks/                   # Jupyter notebooks for prototyping
├── .gitignore                   # Ignored files (e.g., .env, logs)
├── requirements.txt             # Python dependencies
├── README.md                    # Documentation
└── main.py                      # Entry point for the bot
```

---

## Next Steps
### Strategy Development
1. **Advanced Indicators**:
   - Add indicators like RSI, MACD, or Bollinger Bands for more nuanced signals.
   - Experiment with multi-factor strategies.

2. **Backtesting**:
   - Integrate historical data to evaluate strategy performance.

3. **Diversification**:
   - Support multiple cryptocurrencies or equity symbols.
   - Build portfolio-level risk management.

### Risk Management
1. Add dynamic position sizing based on volatility or account equity.
2. Implement trailing stops for better profit locking.

### Performance Monitoring
1. Log trades and results to a database or file for analysis.
2. Create a dashboard to visualize trade performance in real-time.

### Live Data Integration
1. Transition from mock data to real-time data using Alpaca’s API.
2. Test the bot in live market conditions with small capital.

---

## How to Run
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure Environment**:
   - Add your API keys to a `.env` file in the root directory:
     ```
     ALPACA_API_KEY=your_api_key
     ALPACA_API_SECRET=your_api_secret
     ALPACA_BASE_URL=https://paper-api.alpaca.markets
     ```
3. **Run the Bot**:
   ```bash
   python main.py
   ```

---

## Notes
- This bot is currently in development and is optimized for Alpaca’s paper trading environment.
- Use at your own risk for live trading. Ensure strategies are tested thoroughly before deployment.
