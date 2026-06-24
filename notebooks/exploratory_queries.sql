-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. Companies by sector
SELECT sector, COUNT(*) AS company_count
FROM companies
GROUP BY sector
ORDER BY company_count DESC;

-- 3. Top companies by market cap
SELECT *
FROM market_cap
ORDER BY market_cap DESC
LIMIT 10;

-- 4. Top companies by sales
SELECT company_id, year, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;

-- 5. Profit trend by company
SELECT company_id, year, net_profit
FROM profitandloss
ORDER BY company_id, year;

-- 6. Companies with highest cash flow
SELECT company_id, year, operating_cashflow
FROM cashflow
ORDER BY operating_cashflow DESC
LIMIT 10;

-- 7. Stock price sample
SELECT *
FROM stock_prices
LIMIT 20;

-- 8. Financial ratios overview
SELECT *
FROM financial_ratios
LIMIT 20;

-- 9. Documents available by company
SELECT company_id, COUNT(*) AS document_count
FROM documents
GROUP BY company_id
ORDER BY document_count DESC;

-- 10. Pros and cons sample
SELECT *
FROM prosandcons
LIMIT 20;