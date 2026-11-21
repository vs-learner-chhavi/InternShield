from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "sample_offers.csv"

# These words are examples of terms that may indicate risk.
# Their TF-IDF values are used to calculate a text-based warning score.
SUSPICIOUS_TERMS = {
    "fee", "payment", "deposit", "registration", "security",
    "otp", "password", "guaranteed", "urgent", "processing"
}


def load_training_texts():
    import csv

    texts = []
    with open(DATA_PATH, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            texts.append(row["description"])
    return texts


# TF-IDF learns how important words are across the included example offers.
_vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)
_vectorizer.fit(load_training_texts())


def predict_text_risk(text):
    """
    Return a simple TF-IDF-based text warning score from 0 to 100.

    This is a transparent educational score, not a trained fraud classifier
    and not a probability that an offer is fraudulent.
    """
    vector = _vectorizer.transform([text])
    feature_names = _vectorizer.get_feature_names_out()
    values = vector.toarray()[0]

    suspicious_weight = 0.0
    other_weight = 0.0

    for word, value in zip(feature_names, values):
        if word in SUSPICIOUS_TERMS:
            suspicious_weight += float(value)
        else:
            other_weight += float(value)

    total = suspicious_weight + other_weight
    if total == 0:
        return 0.0

    return (suspicious_weight / total) * 100
