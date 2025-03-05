import requests
import pandas as pd
import logging
from config import ALPHA_VANTAGE_API_KEY, DATA_FETCH_INTERVAL

API_URL = "https://www.alphavantage.co/query"

def get_market_data(symbol="EUR/USD", interval=DATA_FETCH_INTERVAL):
    """
    Fetches market data from Alpha Vantage.
    :param symbol: Currency pair or stock symbol.
    :param interval: Time interval (e.g., '1min', '5min').
    :return: Pandas DataFrame with market data.
    """
    params = {
        "apikey": ALPHA_VANTAGE_API_KEY,
        "function": "FX_INTRADAY",
        "from_symbol": symbol.split("/")[0],
        "to_symbol": symbol.split("/")[1],
        "interval": interval,
        "outputsize": "full"
    }
    
    response = requests.get(API_URL, params=params)
    
    if response.status_code != 200:
        logging.error("Error fetching market data: %s", response.text)
        return None
    
    data = response.json()
    time_series = list(data.keys())[-1]
    df = pd.DataFrame.from_dict(data[time_series], orient='index')
    df = df.rename(columns={
        "1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close"
    })
    df = df.astype(float)
    df['timestamp'] = pd.to_datetime(df.index)
    return df
