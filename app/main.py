from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="TIM AI Network Ops MiniLab")

@app.get("/")
def home():
    return {"message": "TIM Network AI Ops API running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    df = pd.read_csv("data/network_metrics.csv")
    return df.to_dict(orient="records")

@app.get("/anomalies")
def anomalies():
    df = pd.read_csv("data/network_metrics_scored.csv")
    bad = df[df["status"] == "ANOMALY"]
    return bad.to_dict(orient="records")