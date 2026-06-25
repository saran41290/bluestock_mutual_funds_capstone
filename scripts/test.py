import sqlite3
import pandas as pd

conn = sqlite3.connect("database/bluestock_mf.db")

for table in [
    "fact_aum",
    "fact_transactions",
    "fact_performance",
    "fact_sip_industry",
    "fact_portfolio"
]:
    print("\n" + "="*50)
    print(table)
    print(pd.read_sql(f"PRAGMA table_info({table})", conn))

conn.close()