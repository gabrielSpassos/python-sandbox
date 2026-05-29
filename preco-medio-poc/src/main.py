from pathlib import Path
import pandas as pd

# Base directory of main.py
BASE_DIR = Path(__file__).resolve().parent

# CSV path
csv_file = BASE_DIR / "resources" / "negociacao-carteira-ate-2025.csv"

# Read CSV
df = pd.read_csv(
    csv_file,
    sep=";",
    encoding="utf-8"
)

print(df.head())

# Read CSV
df = pd.read_csv(
    csv_file,
    sep=",",  # change to ";" if needed
    decimal=",",
    encoding="utf-8"
)

# Clean column names
df.columns = df.columns.str.strip()

# Keep only buy operations
buy_orders = df[df["Tipo de Movimentação"] == "Compra"].copy()

# Convert numeric columns
buy_orders["Quantidade"] = (
    buy_orders["Quantidade"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

buy_orders["Preço"] = (
    buy_orders["Preço"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

buy_orders["Valor"] = (
    buy_orders["Valor"]
    .astype(str)
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

# Group by asset ticker
result = (
    buy_orders.groupby("Código de Negociação")
    .agg(
        quantity=("Quantidade", "sum"),
        total_cost=("Valor", "sum")
    )
    .reset_index()
)

# Calculate average price
result["average_price"] = (
    result["total_cost"] / result["quantity"]
)

# Rename columns
result = result.rename(
    columns={
        "Código de Negociação": "ticker"
    }
)

# Reorder columns
result = result[
    [
        "ticker",
        "quantity",
        "average_price",
        "total_cost"
    ]
]

# Round numeric values
result["average_price"] = result["average_price"].round(2)
result["total_cost"] = result["total_cost"].round(2)

# Print final report
print(result)

# Save result to CSV
result.to_csv("resources/average_price_report.csv", index=False)