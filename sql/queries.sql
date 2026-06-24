-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV Per Month

SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 3. SIP Year-over-Year Growth

SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio Less Than 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;


-- 6. Top 10 Funds by 5-Year Return

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 7. Average Return by Category

SELECT
    category,
    AVG(return_3yr_pct) AS avg_return
FROM scheme_performance
GROUP BY category;


-- 8. Transactions by Payment Mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY payment_mode;


-- 9. Average NAV by AMFI Code

SELECT
    amfi_code,
    AVG(nav) AS average_nav
FROM nav_history
GROUP BY amfi_code;


-- 10. Investor Count by KYC Status

SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM investor_transactions
GROUP BY kyc_status;