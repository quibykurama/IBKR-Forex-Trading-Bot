import pytest
from database.db_connector import insert_trade, fetch_trade_history

def test_insert_trade():
    """
    Tests inserting a trade into the database.
    """
    trade_data = {
        'action': 'BUY',
        'price': 105.25,
        'quantity': 10,
        'timestamp': '2025-03-05 12:00:00'
    }
    insert_trade(trade_data)
    history = fetch_trade_history()
    assert not history.empty
    assert history.iloc[-1]['action'] == 'BUY'

def test_fetch_trade_history():
    """
    Tests retrieving trade history.
    """
    history = fetch_trade_history()
    assert history is not None
    assert isinstance(history, object)  # Ensure it's a DataFrame
