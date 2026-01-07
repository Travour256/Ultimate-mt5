
import time, yaml, MetaTrader5 as mt5, pandas as pd
from system.mt5 import MT5Connector
from system.ai import AIPredictor
from system.governor import Governor
from system.logger import Logger
from system.retrainer import Retrainer

cfg = yaml.safe_load(open("config.yaml"))
logger = Logger()
gov = Governor(cfg)
ai = AIPredictor("models/model.pkl", cfg)
mt5c = MT5Connector(cfg, logger)
rt = Retrainer()

mt5c.connect()

while True:
    data = mt5c.get_market_data(cfg["symbol"])
    decision, confidence = ai.decide(data)

    logger.log_decision(decision, confidence)

    if gov.allow_trade(confidence):
        profit = mt5c.execute_trade(cfg["symbol"], decision)
        gov.record_trade(profit)

    if gov.should_stop():
        logger.log("SYSTEM STOPPED")
        break

    rt.maybe_retrain(gov.stats())
    time.sleep(60)
