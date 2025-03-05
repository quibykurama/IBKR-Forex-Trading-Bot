import logging
import time
from config import TRADING_MODE
from execution.trade_executor import TradeExecutor
from strategies.sma_cross import SMACrossStrategy
from data.data_request import get_market_data

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    """
    Main function to run the trading bot.
    """
    logging.info("Starting trading bot in %s mode", TRADING_MODE)
    
    trade_executor = TradeExecutor()
    strategy = SMACrossStrategy()
    
    while True:
        try:
            # Fetch market data
            market_data = get_market_data()
            
            # Generate trading signals
            signal = strategy.generate_signal(market_data)
            
            # Execute trade based on signal
            if signal:
                trade_executor.execute_trade(signal)
            
            # Sleep before the next iteration (based on strategy settings)
            time.sleep(60)  # Default 1-minute interval
        
        except Exception as e:
            logging.error("An error occurred: %s", e)
            time.sleep(10)  # Pause before retrying


if __name__ == "__main__":
    main()
