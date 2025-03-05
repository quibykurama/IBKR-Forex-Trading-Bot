import os
from dotenv import load_dotenv

# Load environment variables from a .env file (optional for local use)
load_dotenv()

# API Credentials
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")  # Alpha Vantage API Key
IBKR_PAPER_ACCOUNT = os.getenv("IBKR_PAPER_ACCOUNT")  # IBKR Paper Trading Account
IBKR_LIVE_ACCOUNT = os.getenv("IBKR_LIVE_ACCOUNT")  # IBKR Live Trading Account

# Database Connection String
DB_CONN_STRING = os.getenv("DB_CONN_STRING")  # PostgreSQL connection string

# Trading Bot Settings
TRADING_MODE = os.getenv("TRADING_MODE", "PAPER")  # PAPER or LIVE
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")  # Logging Level (DEBUG, INFO, WARNING, ERROR)

# Default Strategy Settings (Can be modified for custom strategies)
DEFAULT_SHORT_SMA = int(os.getenv("DEFAULT_SHORT_SMA", 10))  # Short-term SMA (default: 10)
DEFAULT_LONG_SMA = int(os.getenv("DEFAULT_LONG_SMA", 50))  # Long-term SMA (default: 50)
STOP_LOSS_PERCENTAGE = float(os.getenv("STOP_LOSS_PERCENTAGE", 0.02))  # 2% Stop Loss by default

# Broker API Settings
IBKR_HOST = "127.0.0.1"
IBKR_PORT = 7497  # Paper Trading port (7496 for live trading)

# Data Fetch Interval
DATA_FETCH_INTERVAL = os.getenv("DATA_FETCH_INTERVAL", "1min")  # 1-minute by default
