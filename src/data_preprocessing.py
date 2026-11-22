import pandas as pd
from pathlib import Path

# Locate the dataset
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw" / "internshield_synthetic_dataset.csv"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_PATH = OUTPUT_DIR / "internship_offers.csv"

# Load dataset
df = pd.read_csv(RAW_PATH)

print("Original dataset size:", len(df))

# Check required columns
required_columns = {"description", "is_scam"}

if not required_columns.issubset(df.columns):
    raise ValueError(
        "Dataset must contain 'description' and 'is_scam' columns."
    )

# Keep only the required columns
df = df[["description", "is_scam"]].copy()

# Remove empty descriptions
df["description"] = df["description"].fillna("").astype(str).str.strip()
df = df[df["description"] != ""]

# Convert labels to numeric values
df["is_scam"] = pd.to_numeric(df["is_scam"], errors="coerce")
df = df.dropna(subset=["is_scam"])

# Ensure labels are valid
df = df[df["is_scam"].isin([0, 1])]
df["is_scam"] = df["is_scam"].astype(int)

# Normalize descriptions to identify duplicates
df["_normalized"] = (
    df["description"]
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

# Remove descriptions that have conflicting labels
conflicting = (
    df.groupby("_normalized")["is_scam"]
    .nunique()
)

conflicting_texts = conflicting[conflicting > 1].index
print("Conflicting descriptions:", len(conflicting_texts))

df = df[~df["_normalized"].isin(conflicting_texts)]

# Remove duplicate descriptions
before = len(df)
df = df.drop_duplicates(subset="_normalized", keep="first")
print("Duplicate descriptions removed:", before - len(df))

# Remove temporary column
df = df[["description", "is_scam"]]

# Check that both classes are present
if set(df["is_scam"].unique()) != {0, 1}:
    raise ValueError("Both genuine (0) and fake (1) examples are required.")

# Save processed dataset
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

# Display dataset statistics
print("\n========== DATASET SUMMARY ==========")
print("Total records:", len(df))
print("\nClass distribution:")
print(df["is_scam"].value_counts().sort_index().rename(
    index={0: "Genuine", 1: "Fake"}
))

print("\nUnique descriptions:", df["description"].nunique())
print("Saved to:", OUTPUT_PATH)