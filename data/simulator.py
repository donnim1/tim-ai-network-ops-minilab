import pandas as pd
import random
from datetime import datetime

nodes = [
    "Tower_Rome_1",
    "Tower_Rome_2",
    "Tower_Milan_1",
    "Router_Rome",
    "Router_Milan",
    "Core_Node_1"
]

rows = []

for node in nodes:
    latency = round(random.uniform(10, 40), 2)
    packet_loss = round(random.uniform(0, 2), 2)
    throughput = round(random.uniform(100, 1000), 2)
    cpu = round(random.uniform(20, 90), 2)

    if random.random() < 0.15:
        latency += random.randint(50, 150)
        packet_loss += random.uniform(5, 15)

    rows.append({
        "timestamp": str(datetime.now()),
        "node": node,
        "latency_ms": latency,
        "packet_loss_pct": packet_loss,
        "throughput_mbps": throughput,
        "cpu_usage_pct": cpu
    })

df = pd.DataFrame(rows)
print(df)
df.to_csv("data/network_metrics.csv", index=False)