import logging
import time
from execution.trade_executor import TradeExecutor
from data.data_request import get_market_data
from database.db_connector import fetch_trade_history


def daily_trade_report():
    """
    Generates a daily trade performance report.
    """
    trades = fetch_trade_history()
    if trades is not None and not trades.empty:
        logging.info(f"Total Trades Executed: {len(trades)}")
        logging.info(f"Last Trade: {trades.iloc[-1].to_dict()}")
    else:
        logging.warning("No trades found in history.")

def monitor_bot():
    """
    Monitors bot execution status, logs errors, and performance.
    """
    logging.info("Monitoring bot execution...")
    while True:
        try:
            market_data = get_market_data()
            if market_data is not None:
                logging.info("Market data fetched successfully.")
            else:
                logging.warning("Market data retrieval failed.")
            time.sleep(3600)  # Check every hour
        except Exception as e:
            logging.error(f"Error in bot monitoring: {e}")
            time.sleep(300)  # Wait 5 minutes before retrying
