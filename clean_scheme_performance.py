import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print(df.columns)
print(df.head())

print(df[['return_1yr_pct',
          'return_3yr_pct',
          'return_5yr_pct',
          'expense_ratio_pct']].dtypes)

print("\nNull Values:")
print(df[['return_1yr_pct',
          'return_3yr_pct',
          'return_5yr_pct',
          'expense_ratio_pct']].isnull().sum())

print("\nExpense Ratio Statistics:")
print(df['expense_ratio_pct'].describe())

print("Return 1Y Min:", df['return_1yr_pct'].min())
print("Return 1Y Max:", df['return_1yr_pct'].max())

print("Return 3Y Min:", df['return_3yr_pct'].min())
print("Return 3Y Max:", df['return_3yr_pct'].max())

print("Return 5Y Min:", df['return_5yr_pct'].min())
print("Return 5Y Max:", df['return_5yr_pct'].max())

df.to_csv("data/processed/scheme_performance_cleaned.csv",index=False)