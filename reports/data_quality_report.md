# Data Quality Report

## Project

Bluestock Mutual Funds Capstone

## Objective

To assess and improve the quality of mutual fund datasets before loading them into the SQLite analytical database.

---

# Dataset: NAV History

## Checks Performed

### Date Validation

* Converted date column to datetime format.
* Verified valid date values.

### Duplicate Check

* Identified and removed duplicate records.

### Missing Values

* Checked for missing NAV values.
* Applied forward fill for holidays and weekends where appropriate.

### Business Rule Validation

* Verified NAV values are greater than zero.

### Result

* Dataset cleaned and validated successfully.

---

# Dataset: Investor Transactions

## Checks Performed

### Date Validation

* Converted transaction_date to datetime format.

### Transaction Type Standardization

Standardized values into:

* SIP
* Lumpsum
* Redemption

### Amount Validation

* Verified all transaction amounts are greater than zero.

### KYC Validation

Allowed values:

* Verified
* Pending
* Rejected

### Result

* Dataset cleaned and validated successfully.

---

# Dataset: Scheme Performance

## Checks Performed

### Numeric Validation

Validated:

* return_1yr_pct
* return_3yr_pct
* return_5yr_pct
* alpha
* beta
* sharpe_ratio
* sortino_ratio

### Expense Ratio Validation

Expected Range:

* 0.1% to 2.5%

### Anomaly Detection

* Checked for missing values.
* Flagged extreme or invalid values.

### Result

* Dataset cleaned and validated successfully.

---

# Summary Statistics

| Dataset               | Status |
| --------------------- | ------ |
| NAV History           | Passed |
| Investor Transactions | Passed |
| Scheme Performance    | Passed |

---

# Final Assessment

The datasets passed all major data quality checks and were approved for loading into the SQLite analytical database.
