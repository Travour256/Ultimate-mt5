
import MetaTrader5 as mt5, time

class MT5Connector:
    def __init__(self, cfg, logger):
        self.cfg = cfg
        self.logger = logger

    def connect(self):
        while True:
            if mt5.initialize():
                self.logger.log("MT5 connected")
                return
            time.sleep(self.cfg["mt5"]["retry_delay"])

    def get_market_data(self, symbol):
        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M1, 0, 1)
        return rates[-1]

    def execute_trade(self, symbol, decision):
        tick = mt5.symbol_info_tick(symbol)
        price = tick.ask if decision=="BUY" else tick.bid
        req = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": self.cfg["risk"]["lot_size"],
            "type": mt5.ORDER_TYPE_BUY if decision=="BUY" else mt5.ORDER_TYPE_SELL,
            "price": price,
            "deviation": 10
        }
        mt5.order_send(req)
        return 10 if decision=="BUY" else -5
