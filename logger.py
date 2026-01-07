
import datetime
class Logger:
    def log(self, msg):
        print(datetime.datetime.utcnow(), msg)
    def log_decision(self, d, c):
        self.log(f"Decision={d} Confidence={c}")
