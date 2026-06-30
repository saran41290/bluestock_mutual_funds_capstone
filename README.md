# Mutual Fund Analytics Platform

## Overview

This project is developed as part of the Bluestock Fintech Data Analyst Capstone Program.

The objective is to build an end-to-end Mutual Fund Analytics Platform that:

- Ingests Mutual Fund datasets from multiple sources
- Performs data cleaning and transformation
- Stores data in a structured database
- Computes performance and risk metrics
- Analyzes investor behavior and fund performance
- Builds an interactive dashboard for business insights

---

## Project Structure

```text
bluestock_mutual_funds_capstone/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── scripts/
│
├── sql/
│
├── dashboard/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

## Datasets

The project contains the following datasets:

| Dataset | Description |
|----------|------------|
| 01_fund_master | Mutual Fund master reference data |
| 02_nav_history | Daily NAV history |
| 03_aum_by_fund_house | AUM data by AMC |
| 04_monthly_sip_inflows | SIP industry statistics |
| 05_category_inflows | Category-wise fund inflows |
| 06_industry_folio_count | Industry folio counts |
| 07_scheme_performance | Fund performance metrics |
| 08_investor_transactions | Investor transaction records |
| 09_portfolio_holdings | Mutual fund holdings |
| 10_benchmark_indices | Benchmark index history |

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Requests
- SQLAlchemy
- SQLite
- Jupyter Notebook
- Git & GitHub
- Power BI

---

## Project Progress

### ✅ Day 1
- Project setup
- Data ingestion
- Dataset validation
- Folder structure

### ✅ Day 2
- Data cleaning
- SQLite database design
- Star schema implementation
- SQL analytical queries
- Data dictionary

### ✅ Day 3
- Exploratory Data Analysis (15+ charts)
- NAV trend analysis
- AUM growth analysis
- SIP inflow trend
- Category heatmap
- Investor demographics
- Geographic distribution
- Folio growth
- Correlation matrix
- Sector allocation
- EDA insights

### ✅ Day 4
- Daily return computation
- Annualized return calculation
- CAGR (1Y, 3Y, 5Y)
- Sharpe Ratio
- Sortino Ratio
- Alpha & Beta
- Maximum Drawdown
- Fund Scorecard (0–100)
- Benchmark comparison (Top 5 vs NIFTY50 & NIFTY100)
- Tracking Error analysis

---

## Business Questions

1. Which fund house manages the highest AUM?
2. Which mutual fund generated the highest return?
3. Which category attracts the highest inflows?
4. Which state contributes the highest investments?
5. Which funds outperform benchmark indices?
6. Which AMC has the largest market share?
7. Which fund provides the best risk-adjusted return?
8. How have SIP inflows changed over time?
9. Which age group invests the most?
10. Which fund shows the most consistent performance?

---

## How to Run

Clone repository:

```bash
git clone <repo-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run data ingestion:

```bash
python scripts/data_ingestion.py
```

---

## Author

Saranya D

Data Analyst | Bluestock Fintech Capstone Project