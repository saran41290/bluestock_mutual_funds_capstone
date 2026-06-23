import pandas as pd
from pathlib import Path

RAW = Path("../data/raw")

files = RAW.glob("*.csv")

for file in files:
    df = pd.read_csv(file)

    print("\n")
    print("=" * 50)
    print(file.name)
    print("=" * 50)

    print("Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")

    print(df.head())