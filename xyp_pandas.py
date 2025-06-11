import pandas as pd

df = pd.read_csv("AutoStatistics.csv")

json_data = df.to_json(orient="records", indent=4)
with open("data.json", "w", encoding="utf-8") as f:
    f.write(json_data)