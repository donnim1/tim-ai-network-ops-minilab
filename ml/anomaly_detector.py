import pandas as pd
from sklearn.ensemble import IsolationForest

# Load data
df = pd.read_csv("data/network_metrics.csv")

# Features for AI
features = df[[
    "latency_ms",
    "packet_loss_pct",
    "throughput_mbps",
    "cpu_usage_pct"
]]

# Train model
model = IsolationForest(
    contamination=0.2,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

# Convert labels
df["status"] = df["anomaly"].apply(
    lambda x: "ANOMALY" if x == -1 else "NORMAL"
)

print(df[[
    "node",
    "latency_ms",
    "packet_loss_pct",
    "cpu_usage_pct",
    "status"
]])

# Save result
df.to_csv("data/network_metrics_scored.csv", index=False)