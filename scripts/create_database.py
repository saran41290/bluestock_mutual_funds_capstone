import sqlite3
import pandas as pd

print("STARTING")

try:

    conn = sqlite3.connect(
        "database/bluestock_mf.db"
    )

    print("DB Connected")

    cursor = conn.cursor()

    print("Reading Schema")

    with open("sql/schema.sql") as f:
        schema = f.read()

    print("Schema Loaded")

    cursor.executescript(schema)

    print("Schema Executed")

    conn.commit()

    print("Commit Complete")

    tables = pd.read_sql(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """,
    conn
    )

    print("Tables Found")

    print(tables)

    conn.close()

except Exception as e:
    print("ERROR OCCURRED")
    print(type(e))
    print(e)

print("END")