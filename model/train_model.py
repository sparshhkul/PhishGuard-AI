import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# =====================================
# LOAD DATASET
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "dataset" / "phishing_email.csv"

df = pd.read_csv(DATASET_PATH)

print("\nDataset Loaded Successfully\n")
print(df.head())

print("\nColumns:")
print(df.columns)

# =====================================
# REMOVE UNNECESSARY COLUMN
# =====================================

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# =====================================
# COLUMN NAMES
# =====================================

TEXT_COLUMN = "Email Text"
LABEL_COLUMN = "Email Type"

# =====================================
# REMOVE EMPTY VALUES
# =====================================

df = df.dropna()

# =====================================
# FEATURES & LABELS
# =====================================

X = df[TEXT_COLUMN]

y = df[LABEL_COLUMN]



# =====================================
# ENCODE LABELS
# =====================================

from sklearn.preprocessing import LabelEncoder

# Clean labels
y = y.astype(str).str.strip()

print("\nUnique Labels:")
print(y.unique())

# Convert text labels to numbers
encoder = LabelEncoder()

y = encoder.fit_transform(y)

print("\nEncoded Classes:")
print(encoder.classes_)

print("\nLabel Distribution:")
print(pd.Series(y).value_counts())


# =====================================
# TF-IDF
# =====================================

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000
)

X_vector = vectorizer.fit_transform(X)

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================
# TRAIN MODEL
# =====================================

print("\nTraining Model...\n")

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# =====================================
# TEST MODEL
# =====================================

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\n==============================")
print("MODEL ACCURACY")
print("==============================")

print(f"{accuracy*100:.2f}%")

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

print(classification_report(y_test, prediction))

# =====================================
# SAVE MODEL
# =====================================

MODEL_PATH = BASE_DIR / "model" / "phishing_model.pkl"
VECTORIZER_PATH = BASE_DIR / "model" / "vectorizer.pkl"

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VECTORIZER_PATH)

print("\n==============================")
print("MODEL SAVED SUCCESSFULLY")
print("==============================")

print(f"\nModel File : {MODEL_PATH}")
print(f"Vectorizer : {VECTORIZER_PATH}")