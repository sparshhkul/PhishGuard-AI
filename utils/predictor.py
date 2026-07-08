import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "phishing_model.pkl"
VECTORIZER_PATH = BASE_DIR / "model" / "vectorizer.pkl"

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


def predict_email(email_text):

    email_vector = vectorizer.transform([email_text])

    prediction = model.predict(email_vector)[0]

    probability = model.predict_proba(email_vector)[0]

    risk_score = round(max(probability) * 100)

    if prediction == 1:
        return {
            "label": "Safe Email",
            "risk": risk_score,
            "color": "green"
        }
    else:
        return {
            "label": "Phishing Email",
            "risk": risk_score,
            "color": "red"
        }