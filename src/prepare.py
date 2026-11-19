"""
Stage 1 - prepare.py
Lê data/wine.csv, faz o split treino/teste e salva em data/prepared/
"""
import os, yaml
import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar parâmetros do params.yaml
with open("params.yaml") as f:
    params = yaml.safe_load(f)["prepare"]

df = pd.read_csv("data/wine.csv")

feature_cols = [c for c in df.columns if c not in ["target", "target_name"]]
X = df[feature_cols]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=params["test_size"],
    random_state=params["random_state"],
    stratify=y
)

os.makedirs("data/prepared", exist_ok=True)
X_train.to_csv("data/prepared/X_train.csv", index=False)
X_test.to_csv("data/prepared/X_test.csv",   index=False)
y_train.to_csv("data/prepared/y_train.csv", index=False)
y_test.to_csv("data/prepared/y_test.csv",   index=False)

print(f"Prepare OK: treino={len(X_train)} | teste={len(X_test)}")
