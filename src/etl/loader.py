import pandas as pd
from pathlib import Path
from src.etl.normaliser import normalize_year, normalize_ticker


RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")


def load_excel_file(file_path):
    """Load an Excel file into a Pandas DataFrame."""
    return pd.read_excel(file_path)


def clean_dataframe(df):
    """Clean column names and normalize common fields."""
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "ticker" in df.columns:
        df["ticker"] = df["ticker"].apply(normalize_ticker)

    return df


def save_processed_file(df, output_name):
    """Save cleaned DataFrame to processed folder."""
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_PATH / output_name
    df.to_csv(output_path, index=False)
    return output_path


def process_excel_file(input_file, output_file):
    """Load, clean, and save an Excel file."""
    file_path = RAW_DATA_PATH / input_file
    df = load_excel_file(file_path)
    cleaned_df = clean_dataframe(df)
    return save_processed_file(cleaned_df, output_file)