
class Governor:
    def __init__(self, cfg):
        self.cfg = cfg
        self.trades = 0
        self.wins = 0

    def allow_trade(self, confidence):
        return confidence >= self.cfg["confidence_threshold"]

    def record_trade(self, profit):
        self.trades += 1
        if profit > 0:
            self.wins += 1

    def accuracy(self):
        return self.wins/self.trades if self.trades else 1.0

    def should_stop(self):
        return self.trades and self.accuracy() < self.cfg["accuracy_threshold"]

    def stats(self):
        return {"accuracy": self.accuracy(), "trades": self.trades}
