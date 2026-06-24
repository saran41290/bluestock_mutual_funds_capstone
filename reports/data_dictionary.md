# Data Dictionary – Bluestock Mutual Funds Capstone

## Overview

This document describes the datasets, database tables, column definitions, data types, business meanings, and source references used in the Bluestock Mutual Funds Capstone Project.

---

# Table: dim_fund

**Source:** 01_fund_master.csv

| Column Name       | Data Type | Description                               |
| ----------------- | --------- | ----------------------------------------- |
| amfi_code         | TEXT      | Unique AMFI scheme identifier             |
| fund_house        | TEXT      | Asset Management Company (AMC) name       |
| scheme_name       | TEXT      | Mutual fund scheme name                   |
| category          | TEXT      | Broad category (Equity, Debt, Hybrid)     |
| sub_category      | TEXT      | Detailed category classification          |
| plan              | TEXT      | Growth or Dividend plan                   |
| expense_ratio_pct | REAL      | Annual fund management expense percentage |
| exit_load_pct     | REAL      | Exit fee charged on redemption            |
| risk_category     | TEXT      | Risk classification of the scheme         |

---

# Table: dim_date

**Source:** Generated Calendar Dimension

| Column Name | Data Type | Description                             |
| ----------- | --------- | --------------------------------------- |
| date_id     | INTEGER   | Surrogate date key in YYYYMMDD format   |
| date        | DATE      | Calendar date                           |
| year        | INTEGER   | Calendar year                           |
| month       | INTEGER   | Month number (1–12)                     |
| quarter     | INTEGER   | Quarter number (1–4)                    |
| day_of_week | TEXT      | Day name                                |
| is_weekend  | INTEGER   | Weekend flag (1 = Weekend, 0 = Weekday) |

---

# Table: fact_nav

**Source:** clean_nav_history.csv

| Column Name  | Data Type | Description                                |
| ------------ | --------- | ------------------------------------------ |
| nav_id       | INTEGER   | Unique NAV record identifier               |
| amfi_code    | TEXT      | Mutual fund identifier                     |
| nav_date_id  | INTEGER   | Foreign key to dim_date                    |
| nav          | REAL      | Net Asset Value of the scheme              |
| daily_return | REAL      | Percentage change in NAV from previous day |

---

# Table: fact_transactions

**Source:** clean_transactions.csv

| Column Name      | Data Type | Description                         |
| ---------------- | --------- | ----------------------------------- |
| tx_id            | INTEGER   | Unique transaction identifier       |
| investor_id      | TEXT      | Unique investor identifier          |
| amfi_code        | TEXT      | Mutual fund identifier              |
| tx_date_id       | INTEGER   | Foreign key to dim_date             |
| amount_inr       | REAL      | Transaction amount in Indian Rupees |
| state            | TEXT      | Investor state                      |
| city             | TEXT      | Investor city                       |
| transaction_type | TEXT      | SIP, Lumpsum, or Redemption         |

---

# Table: fact_performance

**Source:** clean_scheme_performance.csv

| Column Name    | Data Type | Description                          |
| -------------- | --------- | ------------------------------------ |
| performance_id | INTEGER   | Unique performance record identifier |
| amfi_code      | TEXT      | Mutual fund identifier               |
| return_1yr_pct | REAL      | 1-Year annualized return percentage  |
| return_3yr_pct | REAL      | 3-Year annualized return percentage  |
| return_5yr_pct | REAL      | 5-Year annualized return percentage  |
| sharpe_ratio   | REAL      | Risk-adjusted return metric          |
| sortino_ratio  | REAL      | Downside risk-adjusted return metric |
| alpha          | REAL      | Excess return relative to benchmark  |
| beta           | REAL      | Volatility relative to benchmark     |

---

# Table: fact_aum

**Source:** 03_aum_by_fund_house.csv

| Column Name | Data Type | Description                             |
| ----------- | --------- | --------------------------------------- |
| aum_id      | INTEGER   | Unique AUM record identifier            |
| fund_house  | TEXT      | Asset Management Company name           |
| date_id     | INTEGER   | Foreign key to dim_date                 |
| aum_crore   | REAL      | Assets Under Management (AUM) in Crores |

---

# Data Quality Checks Performed

## NAV History

* Converted date column to datetime
* Removed duplicate records
* Forward-filled missing NAV values
* Validated NAV values greater than zero

## Investor Transactions

* Standardized transaction types
* Validated positive transaction amounts
* Corrected date formats
* Verified KYC status values

## Scheme Performance

* Converted return metrics to numeric types
* Checked expense ratio range (0.1% – 2.5%)
* Flagged anomalous values
* Verified performance metrics completeness

---

# Business Definitions

**AMC (Asset Management Company)**
Company responsible for managing mutual fund schemes.

**NAV (Net Asset Value)**
Per-unit market value of a mutual fund scheme.

**AUM (Assets Under Management)**
Total value of assets managed by an AMC or mutual fund.

**SIP (Systematic Investment Plan)**
Method of investing fixed amounts periodically into mutual funds.

**Expense Ratio**
Annual fee charged by a mutual fund for management and operational expenses.

**Sharpe Ratio**
Risk-adjusted performance measure comparing excess return to volatility.

**Alpha**
Measure of a fund’s performance relative to its benchmark.

**Beta**
Measure of a fund’s volatility compared to the market.
