import streamlit as st
import pandas as pd
from services.inference.predictor import URLPhishingPredictor
from services.features.url_features import extract_features

# Initialize predictor
predictor = URLPhishingPredictor()

st.title("🔍 Phishing URL Detector")

url = st.text_input("Enter a URL to analyze:")

if st.button("Check URL") and url:
    # Get probability & prediction
    prob = predictor.predict_proba(url)
    label = predictor.predict(url)

    # Show phishing probability
    st.metric("Phishing Probability", f"{prob*100:.2f}%")

    # Verdict thresholds
    if label == 1:
        verdict = "🟥 Phishing"
    elif prob >= 0.5:
        verdict = "🟨 Suspicious"
    else:
        verdict = "🟩 Likely Safe"

    st.subheader(f"Verdict: {verdict}")

    # Extract features for display
    feats = extract_features(url)

    st.write("### Extracted Features")
    st.dataframe(pd.DataFrame(feats).T, use_container_width=True)
