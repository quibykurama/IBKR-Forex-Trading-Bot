import sqlalchemy as db
import pandas as pd
import logging
from config import DB_CONN_STRING

engine = db.create_engine(DB_CONN_STRING)

def insert_trade(trade_data):
    """
    Inserts trade details into the database.
    :param trade_data: Dictionary containing trade details.
    """
    try:
        connection = engine.connect()
        metadata = db.MetaData()
        trades = db.Table('trades', metadata, autoload_with=engine)
        query = db.insert(trades).values(trade_data)
        connection.execute(query)
        connection.close()
        logging.info("Trade inserted successfully.")
    except Exception as e:
        logging.error("Database insert error: %s", e)


def fetch_trade_history():
    """
    Retrieves trade history from the database.
    :return: Pandas DataFrame with trade history.
    """
    try:
        connection = engine.connect()
        df = pd.read_sql("SELECT * FROM trades", connection)
        connection.close()
        return df
    except Exception as e:
        logging.error("Database fetch error: %s", e)
        return None
