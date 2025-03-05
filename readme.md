# Automated Trading Bot

## Overview
This project is a **highly customizable automated trading bot** designed to integrate with **Interactive Brokers (IBKR)** and **Alpha Vantage** for market data and execution. The bot provides a **framework for algorithmic trading**, capable of executing any strategy, including trend-following, mean-reversion, statistical arbitrage, or machine learning-driven strategies. 

By default, it implements a **Simple Moving Average (SMA) Cross Strategy**, demonstrating core trading functionalities, **but can be tailored to any client's trading style and requirements**.

---

## Features
- **Automated Trading Framework**: Execute trades based on fully automated signals.
- **Customizable Trading Strategies**: Supports SMA, MACD, RSI, Bollinger Bands, Mean Reversion, and AI-powered strategies.
- **Multi-Broker Integration**: Works with **IBKR**, **Binance**, and **Alpha Vantage**.
- **Risk Management**: Implements stop-loss, position sizing, and leverage control.
- **Real-time & Historical Market Data**: Fetches data via APIs for both live and backtesting purposes.
- **Database Logging**: Stores trades, positions, and execution details in **PostgreSQL**.
- **Performance Monitoring**: Logs execution history and trading performance.
- **Backtesting & Simulation**: Evaluate strategies before deploying live.
- **Scalable & Modular**: New trading strategies and assets can be easily added.
- **Secure API Management**: Credentials handled via environment variables.

---

## Installation
### **Prerequisites**
- Python 3.8+
- PostgreSQL Database
- API Key from **Alpha Vantage** (for market data)
- Interactive Brokers TWS or IB Gateway (for trade execution)

### **Setup**
1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourgithubusername/trading-bot.git
   cd trading-bot
   ```
2. **Create a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set environment variables**:
   ```sh
   export ALPHA_VANTAGE_API_KEY=your_api_key
   export DB_CONN_STRING='postgresql+psycopg2://user:password@localhost:5432/trading_bot'
   ```
   For Windows (PowerShell):
   ```sh
   $env:ALPHA_VANTAGE_API_KEY="your_api_key"
   $env:DB_CONN_STRING="postgresql+psycopg2://user:password@localhost:5432/trading_bot"
   ```
5. **Run database migrations**:
   ```sh
   python database/models.py
   ```
6. **Start the bot**:
   ```sh
   python run_bot.py
   ```

---

## Project Structure
```
trading_bot/
│── config.py              # Configuration settings (sanitized)
│── setup.py               # Project installation setup
│── requirements.txt       # Dependencies
│── run_bot.py             # Main execution script (Refactored bot.py)
│
├── strategies/
│   │── sma_cross.py       # Default Simple Moving Average (SMA) strategy
│   │── custom_strategy.py # Placeholder for user-defined strategies
│
├── data/
│   │── data_request.py    # Fetches market data (AlphaVantage, IBKR, Dummy)
│   │── historical_data.csv # Sample historical data for backtesting
│
├── execution/
│   │── trade_executor.py  # Executes trades with Interactive Brokers API
│   │── eurekai_ibkr.py    # IBKR trading logic (refactored)
│
├── database/
│   │── db_connector.py    # Handles database connections (PostgreSQL)
│   │── models.py          # Defines database schema for tracking trades
│
├── utils/
│   │── eurekai_utils.py   # Helper functions (timing, logging, etc.)
│   │── eurekai_ops.py     # Routine operations (daily updates, reporting)
│
├── logs/
│   │── bot.log            # Log files for debugging & monitoring
│
├── notebooks/
│   │── backtest_sma.ipynb # Jupyter notebook for strategy backtesting
│
├── tests/
│   │── test_sma.py        # Unit tests for SMA strategy
│   │── test_db.py         # Tests for database operations
│
├── docs/
│   │── README.md          # Documentation for installation, usage, strategy
│   │── TRADE_LOGS.md      # Sample trade logs & performance analysis
│   │── API_REFERENCE.md   # IBKR & AlphaVantage API documentation
```

---

## Trading Strategy: Simple Moving Average (SMA) Cross
This bot uses a **Simple Moving Average (SMA) Cross Strategy** as a **demonstration of functionality**. **The framework is built for full customization**, allowing traders to integrate advanced strategies based on their specific needs.

### **Strategy Explanation**:
- **Moving Averages** smooth out price data, identifying trends over time.
- The strategy is effective in **trending markets** but may underperform in choppy markets.

### **Default Strategy Rules**:
1. **BUY** when **SMA(10) crosses above SMA(50)** (Bullish crossover - indicating upward momentum).
2. **SELL** when **SMA(10) crosses below SMA(50)** (Bearish crossover - indicating downward momentum).
3. **Risk Management**: A stop-loss mechanism ensures controlled exposure to volatility.

### **Custom Strategies**
- Traders can replace the SMA logic with:
  - **Relative Strength Index (RSI)** for momentum-based trading.
  - **MACD (Moving Average Convergence Divergence)** for trend-following.
  - **Bollinger Bands** for volatility-based entries.
  - **Machine Learning Models** for predictive analytics.

---

## Backtesting & Strategy Performance Evaluation
To test the effectiveness of trading strategies, use:
```sh
jupyter notebook notebooks/backtest_sma.ipynb
```
This allows historical data testing, **performance visualization, and optimization tuning**.

---

## Logging & Monitoring
The bot generates logs to track its execution and trading activity:
```sh
cat logs/bot.log
```
For real-time monitoring:
```sh
tail -f logs/bot.log
```

---

## Testing & Validation
To validate the strategy’s functionality and database interactions, run:
```sh
pytest tests/
```
This ensures **trading signals, execution logic, and database storage are all functioning correctly**.

---

## Future Enhancements & Customization Opportunities
- **Support for Additional Brokers**: Binance, Coinbase, Tradestation.
- **AI-Powered Strategies**: Neural networks for predictive trading.
- **Advanced Order Types**: Bracket orders, trailing stops, and limit orders.
- **Multi-Asset Trading**: Crypto, Forex, Stocks, and Commodities.

---

## License
MIT License - Free to use and modify.

---

## Contact
For inquiries, customization requests, or consultation:
📧 **email@example.com** | **GitHub Issues**

Happy Trading! 🚀

