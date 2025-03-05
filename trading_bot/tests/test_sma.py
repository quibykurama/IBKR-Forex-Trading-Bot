import pytest
import pandas as pd
from strategies.sma_cross import SMACrossStrategy

def test_sma_cross_strategy():
    """
    Test that SMA cross strategy correctly generates buy/sell signals.
    """
    data = {
        'close': [100, 102, 104, 106, 108, 110, 107, 105, 103, 101]
    }
    df = pd.DataFrame(data)
    
    strategy = SMACrossStrategy(short_window=3, long_window=5)
    signal = strategy.generate_signal(df)
    
    assert signal is not None
    assert signal['action'] in ['BUY', 'SELL']
