-- 1. Overall totals: revenue, cost, gross profit, gross margin
SELECT
    COUNT(*) AS transactions,
    ROUND(SUM(revenue), 2) AS total_revenue,
    ROUND(SUM(cost), 2) AS total_cost,
    ROUND(SUM(revenue) - SUM(cost), 2) AS gross_profit,
    ROUND(100.0 * (SUM(revenue) - SUM(cost)) / SUM(revenue), 1) AS margin_pct
FROM financial_transactions;

-- 2. Monthly revenue and margin trend
SELECT
    substr(transaction_date, 1, 7) AS month,
    COUNT(*) AS deals,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(AVG(revenue), 2) AS avg_deal,
    ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct
FROM financial_transactions
GROUP BY month
ORDER BY month;

-- 3. Performance by category
SELECT
    category,
    COUNT(*) AS deals,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(100.0 * SUM(revenue) / (SELECT SUM(revenue) FROM financial_transactions), 1) AS share_pct,
    ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct
FROM financial_transactions
GROUP BY category
ORDER BY revenue DESC;

-- 4. Performance by product
SELECT
    product,
    category,
    COUNT(*) AS deals,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct
FROM financial_transactions
GROUP BY product, category
ORDER BY revenue DESC;

-- 5. Performance by region
SELECT
    region,
    COUNT(*) AS deals,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(100.0 * SUM(revenue) / (SELECT SUM(revenue) FROM financial_transactions), 1) AS share_pct,
    ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct
FROM financial_transactions
GROUP BY region
ORDER BY revenue DESC;

-- 6. Top 10 customers by revenue
SELECT
    customer,
    COUNT(*) AS deals,
    ROUND(SUM(revenue), 2) AS revenue,
    ROUND(100.0 * SUM(revenue) / (SELECT SUM(revenue) FROM financial_transactions), 1) AS share_pct
FROM financial_transactions
GROUP BY customer
ORDER BY revenue DESC
LIMIT 10;
