from pathlib import Path
import pandas as pd


def parse_brl_number(value):
    return (
        str(value)
        .replace("R$", "")
        .replace(".", "")
        .replace(",", ".")
        .strip()
    )


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
    .apply(parse_brl_number)
    .astype(float)
)

buy_orders["Valor"] = (
    buy_orders["Valor"]
    .apply(parse_brl_number)
    .astype(float)
)

# Group by asset
result = (
    buy_orders.groupby("Código de Negociação")
    .agg(
        quantidade=("Quantidade", "sum"),
        custo_total=("Valor", "sum")
    )
    .reset_index()
)

# Calculate average price
result["preco_medio"] = (
    result["custo_total"] / result["quantidade"]
)

# Rename columns to Portuguese
result = result.rename(
    columns={
        "Código de Negociação": "ativo"
    }
)

# Reorder columns
result = result[
    [
        "ativo",
        "quantidade",
        "preco_medio",
        "custo_total"
    ]
]

# Round values
result["preco_medio"] = result["preco_medio"].round(2)
result["custo_total"] = result["custo_total"].round(2)

# Save result to CSV
output_file = BASE_DIR / "resources" / "preco_medio.csv"
result.to_csv(output_file, index=False)
