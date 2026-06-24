import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

print(df["transaction_type"].unique())

print(df["kyc_status"].unique())

print(df["amount_inr"].describe())

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print(df["transaction_date"].dtype)

df.to_csv("data/processed/investor_transactions_cleaned.csv", index=False)
print(df.info())