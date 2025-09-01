import pandas as pd
import json
import os

# Paths
input_csv = os.path.join(os.path.dirname(__file__), "../resource/input.csv")
output_json = os.path.join(os.path.dirname(__file__), "../resource/output.json")

# Read CSV
df = pd.read_csv(input_csv)

# Column to extract
column_name = "id"  # replace with your CSV header

json_object = {
    "method": "POST",
    "url": "https://localhost:8080/api/$id"
}

# Create list of JSON objects
json_list = [
    {
        **json_object,
        "url": json_object["url"].replace("$id", str(val))
    }
    for val in df[column_name].tolist()
]

# Save JSON
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(json_list, f, ensure_ascii=False, indent=4)

print(f"Saved {len(json_list)} JSON objects to {output_json}")
