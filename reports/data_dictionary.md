# Data Dictionary

## Project

Bluestock Mutual Funds Capstone

---

# Dimension Tables

## dim_fund

| Column            | Type | Description             |
| ----------------- | ---- | ----------------------- |
| amfi_code         | TEXT | Unique AMFI Scheme Code |
| fund_house        | TEXT | Mutual Fund House       |
| scheme_name       | TEXT | Scheme Name             |
| category          | TEXT | Mutual Fund Category    |
| sub_category      | TEXT | Detailed Category       |
| plan              | TEXT | Growth/Dividend Plan    |
| expense_ratio_pct | REAL | Expense Ratio (%)       |
| exit_load_pct     | REAL | Exit Load (%)           |
| risk_category     | TEXT | Risk Classification     |

Source:
01_fund_master.csv

---

## dim_date

| Column      | Type    | Description       |
| ----------- | ------- | ----------------- |
| date_id     | INTEGER | YYYYMMDD Date Key |
| date        | DATE    | Calendar Date     |
| year        | INTEGER | Year              |
| month       | INTEGER | Month             |
| quarter     | INTEGER | Quarter           |
| day_of_week | TEXT    | Day Name          |
| is_weekend  | INTEGER | Weekend Flag      |

Generated using create_dim_date.py

---

# Fact Tables

## fact_nav

Source:
clean_nav_history.csv

| Column           | Type    | Description          |
| ---------------- | ------- | -------------------- |
| amfi_code        | TEXT    | Scheme Code          |
| nav_date_id      | INTEGER | Date Key             |
| nav              | REAL    | Net Asset Value      |
| daily_return_pct | REAL    | Daily NAV Return (%) |

---

## fact_transactions

Source:
clean_transactions.csv

| Column           | Type    | Description            |
| ---------------- | ------- | ---------------------- |
| tx_id            | INTEGER | Transaction ID         |
| investor_id      | TEXT    | Investor ID            |
| date             | DATE    | Transaction Date       |
| amfi_code        | TEXT    | Scheme Code            |
| amount_inr       | REAL    | Transaction Amount     |
| state            | TEXT    | Investor State         |
| city             | TEXT    | Investor City          |
| transaction_type | TEXT    | SIP/Lumpsum/Redemption |

---

## fact_performance

Source:
clean_scheme_performance.csv

| Column           | Type | Description      |
| ---------------- | ---- | ---------------- |
| amfi_code        | TEXT | Scheme Code      |
| return_1yr_pct   | REAL | 1-Year Return    |
| return_3yr_pct   | REAL | 3-Year Return    |
| return_5yr_pct   | REAL | 5-Year Return    |
| sharpe_ratio     | REAL | Sharpe Ratio     |
| sortino_ratio    | REAL | Sortino Ratio    |
| alpha            | REAL | Alpha            |
| beta             | REAL | Beta             |
| max_drawdown_pct | REAL | Maximum Drawdown |

---

## fact_aum

Source:
03_aum_by_fund_house.csv

| Column      | Type    | Description             |
| ----------- | ------- | ----------------------- |
| fund_house  | TEXT    | AMC Name                |
| date_id     | INTEGER | Date Key                |
| aum_crore   | REAL    | Assets Under Management |
| num_schemes | INTEGER | Number of Schemes       |

---

## fact_sip_industry

Source:
04_monthly_sip_inflows.csv

| Column                    | Type | Description           |
| ------------------------- | ---- | --------------------- |
| month                     | TEXT | Month                 |
| sip_inflow_crore          | REAL | Monthly SIP Inflow    |
| active_sip_accounts_crore | REAL | Active SIP Accounts   |
| new_sip_accounts_lakh     | REAL | New SIP Accounts      |
| sip_aum_lakh_crore        | REAL | SIP AUM               |
| yoy_growth_pct            | REAL | Year-over-Year Growth |

---

## fact_portfolio

Source:
09_portfolio_holdings.csv

| Column         | Type | Description             |
| -------------- | ---- | ----------------------- |
| amfi_code      | TEXT | Scheme Code             |
| stock_symbol   | TEXT | Stock Ticker            |
| weight_pct     | REAL | Portfolio Weight (%)    |
| sector         | TEXT | Industry Sector         |
| portfolio_date | DATE | Portfolio Snapshot Date |

---

# Data Quality Checks

* Removed duplicate records
* Converted date columns to datetime
* Standardized transaction types
* Validated NAV > 0
* Validated transaction amount > 0
* Validated expense ratio
* Converted return columns to numeric
* Created Date Dimension
* Loaded cleaned data into SQLite Star Schema

---

# Database Summary

Dimensions

* dim_fund
* dim_date

Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum
* fact_sip_industry
* fact_portfolio

```
```
