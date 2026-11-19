"""
Stage 2 - train.py
Lê data/prepared/, treina o modelo e salva em artifacts/
"""
import os, json, yaml
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib

with open("params.yaml") as f:
    params = yaml.safe_load(f)["train"]

X_train = pd.read_csv("data/prepared/X_train.csv")
X_test  = pd.read_csv("data/prepared/X_test.csv")
y_train = pd.read_csv("data/prepared/y_train.csv").squeeze()
y_test  = pd.read_csv("data/prepared/y_test.csv").squeeze()

model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf",    RandomForestClassifier(
        n_estimators=params["n_estimators"],
        random_state=params["random_state"]
    ))
])
model.fit(X_train, y_train)

y_pred   = model.predict(X_test)
accuracy = round(float(accuracy_score(y_test, y_pred)), 4)
f1       = round(float(f1_score(y_test, y_pred, average="macro")), 4)

os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/model.joblib")

metrics = {"accuracy": accuracy, "f1_macro": f1}
with open("artifacts/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"Train OK: accuracy={accuracy} | f1={f1}")
