import sqlite3
import pandas as pd

conn = sqlite3.connect("nifty100.db")

query = """
SELECT
    company_id,
    MIN(year) AS min_year,
    MAX(year) AS max_year,
    COUNT(year) AS total_years
FROM financial_ratios
GROUP BY company_id
ORDER BY total_years
"""

df = pd.read_sql(query, conn)

print(df.head(20))

conn.close()