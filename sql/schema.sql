--Task1
/*write CREATE TABLE statements for dim_fund, dim_date, fact_nav, fact_transactions, 
fact_performance, fact_aum. Define primary and foreign keys.*/
--dim_fund
CREATE TABLE IF NOT EXISTS dim_fund(
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    risk_category TEXT
);
--dim_date
CREATE TABLE IF NOT EXISTS dim_date(
    date_id INTEGER PRIMARY KEY,
    date DATE,
    year INTEGER,
    month INTEGER,
    quarter INTEGER,
    day_of_week TEXT,
    is_weekend INTEGER
);
--fact_nav
CREATE TABLE IF NOT EXISTS fact_nav(
    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    nav_date_id INTEGER,
    nav REAL,
    daily_return REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(nav_date_id) REFERENCES dim_date(date_id)
);
--fact_transactions
CREATE TABLE IF NOT EXISTS fact_transactions(
    tx_id INTEGER PRIMARY KEY,
    investor_id TEXT,
    amfi_code TEXT,
    tx_date_id INTEGER,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    transaction_type TEXT,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(tx_date_id) REFERENCES dim_date(date_id)
);
--fact_performance
CREATE TABLE IF NOT EXISTS fact_performance(
    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    alpha REAL,
    beta REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

--fact_aum
CREATE TABLE IF NOT EXISTS fact_aum (
    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house TEXT,
    date_id INTEGER,
    aum_crore REAL
);
--fact sip_inflows
CREATE TABLE IF NOT EXISTS fact_sip_inflows(
    sip_date_id INTEGER,
    sip_amount_crore REAL,
    FOREIGN KEY(sip_date_id) REFERENCES dim_date(date_id)
);

