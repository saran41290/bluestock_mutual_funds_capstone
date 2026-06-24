import pandas as pd

print("Creating Date Dimension...")

dates = pd.date_range(
    start="2020-01-01",
    end="2030-12-31",
    freq="D"
)

dim_date = pd.DataFrame()

dim_date["date"] = dates

dim_date["date_id"] = (
    dim_date["date"]
    .dt.strftime("%Y%m%d")
    .astype(int)
)

dim_date["year"] = dim_date["date"].dt.year

dim_date["month"] = dim_date["date"].dt.month

dim_date["quarter"] = dim_date["date"].dt.quarter

dim_date["day_of_week"] = (
    dim_date["date"].dt.day_name()
)

dim_date["is_weekend"] = (
    dim_date["date"].dt.dayofweek >= 5
).astype(int)

dim_date = dim_date[
[
    "date_id",
    "date",
    "year",
    "month",
    "quarter",
    "day_of_week",
    "is_weekend"
]
]

dim_date.to_csv(
    "data/processed/dim_date.csv",
    index=False
)

print("dim_date.csv created")
print(f"Rows: {len(dim_date)}")
print(dim_date.head())