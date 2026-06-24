# Data Dictionary

## 1. nav_history

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI code for mutual fund |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value of the scheme |

---

## 2. investor_transactions

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund AMFI code |
| transaction_type | TEXT | SIP, Lumpsum, Redemption |
| amount_inr | INTEGER | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier classification of city |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI, Net Banking, etc. |
| kyc_status | TEXT | Verified or Pending |

---

## 3. scheme_performance

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund AMFI code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| plan | TEXT | Regular or Direct plan |
| return_1yr_pct | REAL | 1-year return percentage |
| return_3yr_pct | REAL | 3-year return percentage |
| return_5yr_pct | REAL | 5-year return percentage |
| benchmark_3yr_pct | REAL | Benchmark return |
| alpha | REAL | Alpha measure |
| beta | REAL | Beta measure |
| sharpe_ratio | REAL | Risk-adjusted return |
| sortino_ratio | REAL | Downside risk-adjusted return |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | INTEGER | Assets Under Management (Crores) |
| expense_ratio_pct | REAL | Expense ratio percentage |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk category |