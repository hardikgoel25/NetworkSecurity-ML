import joblib
from services.features.url_features import extract_features

class URLPhishingPredictor:
    def __init__(self):
        self.preprocessor = joblib.load("final_model/preprocessor.pkl")
        self.model = joblib.load("final_model/model.pkl")

    def predict(self, url: str):
        feats = extract_features(url)                     # (1,30) DataFrame
        feats_proc = self.preprocessor.transform(feats)   # preprocessing
        return self.model.predict(feats_proc)[0]

    def predict_proba(self, url: str):
        feats = extract_features(url)
        feats_proc = self.preprocessor.transform(feats)
        if hasattr(self.model, "predict_proba"):          # not all models support it
            return self.model.predict_proba(feats_proc)[0][1]  # probability of phishing (class=1)
        else:
            # fallback: use decision_function or just return predict()
            return float(self.model.predict(feats_proc)[0])
