import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(by=["amfi_code", "date"]).reset_index(drop=True)

print(df.info())
print(df.head())

invalid_nav = df[df["nav"] <= 0]

print("Invalid NAV rows:")
print(invalid_nav)

print("Count:", len(invalid_nav))

df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

