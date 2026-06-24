import pandas as pd
import sqlite3
from sqlalchemy import create_engine
conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

cursor = conn.cursor()

cursor.executescript("""
DELETE FROM fact_nav;
DELETE FROM fact_transactions;
DELETE FROM fact_performance;
DELETE FROM fact_aum;
DELETE FROM dim_date;
DELETE FROM dim_fund;
""")

conn.commit()
conn.close()

print("=" * 60)
print("BLUESTOCK MUTUAL FUND DATABASE LOADER")
print("=" * 60)

# DATABASE CONNECTION
engine = create_engine(
    "sqlite:///database/bluestock_mf.db"
)
print("Connected to SQLite Database")


# LOAD DIM_FUND
fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund = fund[
[
    "amfi_code",
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "expense_ratio_pct",
    "exit_load_pct",
    "risk_category"
]
]

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print(f"dim_fund loaded : {len(fund)} rows")

# LOAD DIM_DATE
date_df = pd.read_csv(
    "data/processed/dim_date.csv"
)

date_df.to_sql(
    "dim_date",
    engine,
    if_exists="append",
    index=False
)
print(f"dim_date loaded : {len(date_df)} rows")

# LOAD FACT_NAV
nav = pd.read_csv(
    "data/processed/clean_nav_history.csv"
)
nav["date"] = pd.to_datetime(
    nav["date"]
)
nav["nav_date_id"] = (
    nav["date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)
nav = nav.sort_values(
    ["amfi_code", "date"]
)
nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)
nav = nav[
[
    "amfi_code",
    "nav_date_id",
    "nav",
    "daily_return"
]
]
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)
print(f"fact_nav loaded : {len(nav)} rows")


# LOAD FACT_TRANSACTIONS
tx = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"]
)

tx["tx_date_id"] = (
    tx["transaction_date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

tx = tx[
[
    "investor_id",
    "amfi_code",
    "tx_date_id",
    "amount_inr",
    "state",
    "city",
    "transaction_type"
]
]

tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print(f"fact_transactions loaded : {len(tx)} rows")


# LOAD FACT_PERFORMANCE
perf = pd.read_csv(
    "data/processed/clean_scheme_performance.csv"
)

perf = perf[
[
    "amfi_code",
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "sharpe_ratio",
    "sortino_ratio",
    "alpha",
    "beta"
]
]

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print(f"fact_performance loaded : {len(perf)} rows")


# LOAD FACT_AUM
aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum["date"] = pd.to_datetime(
    aum["date"]
)

aum["date_id"] = (
    aum["date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

aum = aum[
[
    "fund_house",
    "date_id",
    "aum_crore"
]
]

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="append",
    index=False
)

print(f"fact_aum loaded : {len(aum)} rows")


# VERIFY COUNTS


print("\n")
print("=" * 60)
print("TABLE ROW COUNTS")
print("=" * 60)

conn = sqlite3.connect(
    "database/bluestock_mf.db"
)

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        conn
    )

    print(
        f"{table:<20} {count['cnt'][0]}"
    )

conn.close()

print("\nDatabase Load Complete")