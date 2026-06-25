/*
--Task3
Write 10 analytical SQL queries — 
top 5 funds by AUM, 
average NAV per month, 
SIP YoY growth, 
transactions by state, 
funds with expense_ratio < 1%, and 
5 more of your choice.
--------------------------------------------------------------------------------------------
*/
--top 5 funds by AUM, 
select fund_house,sum(aum_crore) as total_aum 
from fact_aum group by fund_house 
order by total_aum desc limit 5;
------------------------------------------------------------------------------
--average NAV per month
select * from fact_nav;
select d.month,avg(fnav.nav) as avg_nav from fact_nav fnav 
join dim_date d on fnav.nav_date_id=d.date_id
group by d.month;
-----------------------------------------------------------
--SIP YoY growth
select month, sip_inflow_crore, yoy_growth_pct
from fact_sip_industry  order by month;

-----------------------------------------------------------
--transactions by state 
select * from fact_transactions;
select state,count(*) as total_txns,
sum(amount_inr) as total_amount 
from fact_transactions
group by state order by total_txns  desc;
-----------------------------------------------------------
--funds with expense_ratio < 1%
select fund_house,expense_ratio_pct from dim_fund where 
expense_ratio_pct < 1;
-----------------------------------------------------------
--Top 10 Funds by 5-Year Return
select
    p.amfi_code,d.scheme_name,p.return_5yr_pct
from fact_performance p
join dim_fund d on p.amfi_code = d.amfi_code
order by p.return_5yr_pct desc
limit 10;
-----------------------------------------------------------
-----------------------------------------------------------
--Average Transaction Amount by Transaction Type
select transaction_type,round(avg(amount_inr),2) as avg_amt 
from fact_transactions group by
transaction_type order by avg_amt desc;
-----------------------------------------------------------
-----------------------------------------------------------
--Top 10 Cities by Investment Amount
select city,sum(amount_inr) as total_amt 
from fact_transactions group by
city order by total_amt desc
limit 10;
-----------------------------------------------------------
--Fund Count by Risk Category
select risk_category,count(*) as fund_count
from dim_fund
group by risk_category
order by fund_count desc;
------------------------------------------------------------
--Monthly Transaction Trend
select
    strftime('%Y',date) as year, 
    strftime('%m',date) as month, COUNT(*) as transaction_count, 
    ROUND(SUM(amount_inr),2) as total_amount
from fact_transactions 
group by year,month
order by year,month;
--------------------------------------------------------------------------
