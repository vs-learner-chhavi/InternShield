
from pathlib import Path
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "processed" / "internship_offers.csv"
MODEL_DIR = BASE_DIR / "models"

MODEL_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_PATH)

X = df["description"]
y = df["is_scam"]

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=20000,
    min_df=2
)

X_vectors = vectorizer.fit_transform(X)

model = MultinomialNB(alpha=1.0)
model.fit(X_vectors, y)

joblib.dump(vectorizer, MODEL_DIR / "tfidf_vectorizer.pkl")
joblib.dump(model, MODEL_DIR / "naive_bayes_model.pkl")

print("Model training completed.")
print("Total training records:", len(X))
print("Genuine records:", (y == 0).sum())
print("Fake records:", (y == 1).sum())
print("Model saved successfully.")
