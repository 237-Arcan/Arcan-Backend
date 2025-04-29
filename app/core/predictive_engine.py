# app/core/predictive_engine.py
from sklearn.linear_model import LogisticRegression
import pandas as pd

def fetch_live_odds():
    # Placeholder: Simule des données live
    df = pd.read_csv("data/live_odds_simulated.csv")
    return df.set_index("timestamp")["odds"]

def train_predictive_model(data):
    X = data[["team_rating", "momentum", "home_advantage"]]
    y = data["result"]
    model = LogisticRegression()
    model.fit(X, y)
    return model
