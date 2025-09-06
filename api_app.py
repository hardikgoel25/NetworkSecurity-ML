from flask import Flask, request, jsonify
from services.features.url_features import extract_features
from services.inference.predictor import URLPhishingPredictor

app = Flask(__name__)
predictor = URLPhishingPredictor()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "Missing URL"}), 400

    url = data["url"]
    feats = extract_features(url)
    prob = predictor.predict_proba(feats)

    return jsonify({
        "url": url,
        "probability": prob,
        "features": feats
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
