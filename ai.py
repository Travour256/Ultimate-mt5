
import joblib, numpy as np

class AIPredictor:
    def __init__(self, model_path, cfg):
        self.model = joblib.load(model_path)
        self.cfg = cfg

    def decide(self, data):
        X = np.array([[data['open'], data['high'], data['low'], data['close'], data['tick_volume'], data['spread']]])
        probs = self.model.predict_proba(X)[0]
        label = int(np.argmax(probs))
        confidence = probs[label]
        return ("BUY" if label==1 else "SELL"), confidence
