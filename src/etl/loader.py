import pandas as pd
from pathlib import Path
from src.etl.normaliser import normalize_year, normalize_ticker

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")


FILES_TO_PROCESS = [
    "analysis",
    "balancesheet",
    "cashflow",
    "companies",
    "documents",
    "profitandloss",
    "prosandcons",
    "financial_ratios",
    "market_cap",
    "peer_groups",
    "sectors",
    "stock_prices",
]


def clean_column_name(col):
    """Clean column names into database-friendly format."""
    return (
        str(col)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace("/", "_")
        .replace("%", "pct")
        .replace(".", "")
    )


def load_excel_file(file_path):
    """Load Excel file into DataFrame."""
    return pd.read_excel(file_path)


def clean_dataframe(df):
    """Clean dataframe columns and normalize common fields."""
    df = df.copy()

    df.columns = [clean_column_name(col) for col in df.columns]

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "ticker" in df.columns:
        df["ticker"] = df["ticker"].apply(normalize_ticker)

    return df


def process_all_excels():
    """Convert all raw Excel files into processed CSV files."""
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    for file_stem in FILES_TO_PROCESS:
        input_path = RAW_DATA_PATH / f"{file_stem}.xlsx"
        output_path = PROCESSED_DATA_PATH / f"{file_stem}.csv"

        if not input_path.exists():
            print(f"Missing file: {input_path}")
            continue

        df = load_excel_file(input_path)
        df = clean_dataframe(df)
        df.to_csv(output_path, index=False)

        print(f"Processed {file_stem}.xlsx → {file_stem}.csv | Rows: {len(df)}")


if __name__ == "__main__":
    process_all_excels()