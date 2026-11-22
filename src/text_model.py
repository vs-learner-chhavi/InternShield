from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

vectorizer = joblib.load(
    MODEL_DIR / "tfidf_vectorizer.pkl"
)

model = joblib.load(
    MODEL_DIR / "naive_bayes_model.pkl"
)

SUSPICIOUS_TERMS = {
    "fee", "payment", "deposit", "registration",
    "security", "otp", "password", "guaranteed",
    "urgent", "processing"
}


def predict_text_risk(text):
    vector = vectorizer.transform([text])

    feature_names = vectorizer.get_feature_names_out()
    values = vector.toarray()[0]

    suspicious_weight = 0.0
    total_weight = 0.0

    for word, value in zip(feature_names, values):
        total_weight += float(value)

        if word in SUSPICIOUS_TERMS:
            suspicious_weight += float(value)

    if total_weight == 0:
        return 0.0

    return (suspicious_weight / total_weight) * 100


def predict_scam(text):
    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]
    probabilities = model.predict_proba(vector)[0]

    scam_index = list(model.classes_).index(1)

    scam_score = probabilities[scam_index] * 100

    result = "Likely Fake" if prediction == 1 else "Likely Genuine"

    return round(float(scam_score), 2), result
