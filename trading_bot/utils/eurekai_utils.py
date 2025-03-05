import logging
import time
from datetime import datetime

# Configure Logging
logging.basicConfig(filename='logs/bot.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(message, level="info"):
    """
    Logs an event to the bot's log file.
    :param message: Log message.
    :param level: Log level (info, warning, error, debug).
    """
    levels = {
        "info": logging.info,
        "warning": logging.warning,
        "error": logging.error,
        "debug": logging.debug
    }
    if level in levels:
        levels[level](message)
    else:
        logging.info(message)

def time_selector(interval='1min'):
    """
    Determines sleep time based on the bot's interval.
    """
    interval_map = {
        '1min': 60,
        '5min': 300,
        '15min': 900,
        '30min': 1800,
        '60min': 3600,
    }
    return interval_map.get(interval, 60)

def bot_sleep(sleep_time):
    """
    Puts the bot to sleep for the given duration.
    """
    logging.info(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)
