import logging
from execution.eurekai_ibkr import TradingApp, make_order
from config import TRADING_MODE, IBKR_HOST, IBKR_PORT

class TradeExecutor:
    """
    Handles trade execution through Interactive Brokers API.
    """
    def __init__(self):
        self.app = None
        
    def connect_to_ibkr(self):
        """
        Establishes a connection to the IBKR trading platform.
        """
        if not self.app:
            self.app = TradingApp()
            self.app.connect(IBKR_HOST, IBKR_PORT, clientId=1 if TRADING_MODE == "PAPER" else 2)
            logging.info("Connected to IBKR.")
        
    def execute_trade(self, signal):
        """
        Executes a trade based on the provided signal.
        :param signal: Dict containing 'action' ('BUY' or 'SELL') and 'price'.
        """
        if not signal:
            logging.warning("No trade signal received. Skipping execution.")
            return
        
        self.connect_to_ibkr()
        
        action = signal['action']
        price = signal['price']
        quantity = 10  # Example trade size, should be dynamic based on portfolio size
        
        order = make_order(orderId=self.app.nextValidOrderId, orderType="MKT", action=action, totalQuantity=quantity)
        contract = self.app.create_contract("EUR", "CASH", "USD", "IDEALPRO")
        
        logging.info(f"Placing {action} order for {quantity} units at {price}.")
        self.app.placeOrder(order.orderId, contract, order)
        
    def disconnect(self):
        """
        Disconnect from IBKR.
        """
        if self.app:
            self.app.disconnect()
            logging.info("Disconnected from IBKR.")
