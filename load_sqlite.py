import sqlite3
import pandas as pd

# Connect database
conn = sqlite3.connect("bluestock_mf.db")

# Load cleaned CSV files
nav_df = pd.read_csv(
    "data/processed/nav_history_cleaned.csv"
)

txn_df = pd.read_csv(
    "data/processed/investor_transactions_cleaned.csv"
)

perf_df = pd.read_csv(
    "data/processed/scheme_performance_cleaned.csv"
)

# Insert into SQLite tables

nav_df.to_sql(
    "nav_history",
    conn,
    if_exists="replace",
    index=False
)

txn_df.to_sql(
    "investor_transactions",
    conn,
    if_exists="replace",
    index=False
)

perf_df.to_sql(
    "scheme_performance",
    conn,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")

conn.close()