import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "nifty100.db"
PROCESSED_PATH = Path("data/processed")
OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)


TABLE_FILES = {
    "companies": "companies.csv",
    "sectors": "sectors.csv",
    "profitandloss": "profitandloss.csv",
    "balancesheet": "balancesheet.csv",
    "cashflow": "cashflow.csv",
    "analysis": "analysis.csv",
    "documents": "documents.csv",
    "prosandcons": "prosandcons.csv",
    "stock_prices": "stock_prices.csv",
    "financial_ratios": "financial_ratios.csv",
}


def load_csv_to_sqlite():
    conn = sqlite3.connect(DB_PATH)
    audit_rows = []

    for table_name, file_name in TABLE_FILES.items():
        file_path = PROCESSED_PATH / file_name

        if not file_path.exists():
            audit_rows.append({
                "table_name": table_name,
                "file_name": file_name,
                "status": "missing",
                "rows_loaded": 0
            })
            continue

        df = pd.read_csv(file_path)

        df.to_sql(table_name, conn, if_exists="replace", index=False)

        audit_rows.append({
            "table_name": table_name,
            "file_name": file_name,
            "status": "loaded",
            "rows_loaded": len(df)
        })

        print(f"{table_name} loaded successfully: {len(df)} rows")

    audit_df = pd.DataFrame(audit_rows)
    audit_df.to_csv(OUTPUT_PATH / "load_audit.csv", index=False)

    conn.close()
    print("Data loading completed. Audit file created.")


if __name__ == "__main__":
    load_csv_to_sqlite()