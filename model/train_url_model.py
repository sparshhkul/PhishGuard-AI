import pandas as pd
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# =====================================
# LOAD DATASET
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "dataset" / "phishing.csv"

df = pd.read_csv(DATASET_PATH)

print("\nDataset Loaded Successfully\n")

print(df.head())

print("\nColumns:\n")

print(df.columns)

# =====================================
# REMOVE INDEX
# =====================================

if "Index" in df.columns:
    df = df.drop(columns=["Index"])

# =====================================
# FEATURES & LABEL
# =====================================

X = df.drop(columns=["class"])

y = df["class"]

# Convert labels

y = y.replace({
    -1: 1,   # Phishing
     1: 0    # Legitimate
})

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# =====================================
# MODEL
# =====================================

print("\nTraining URL Model...\n")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# =====================================
# EVALUATION
# =====================================

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print("\n==============================")
print("URL MODEL ACCURACY")
print("==============================")

print(f"{accuracy*100:.2f}%")

print("\n==============================")
print("CLASSIFICATION REPORT")
print("==============================")

print(classification_report(y_test, prediction))

# =====================================
# SAVE MODEL
# =====================================

MODEL_PATH = BASE_DIR / "model" / "url_model.pkl"

joblib.dump(model, MODEL_PATH)

print("\nModel Saved Successfully")

print(MODEL_PATH)