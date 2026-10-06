-- financial_transactions schema (SQLite)
-- Matches the real database at data/financial_analysis.db
-- and the CSV export at data/financial_transactions.csv.

DROP TABLE IF EXISTS financial_transactions;

CREATE TABLE financial_transactions (
    transaction_id INTEGER PRIMARY KEY,
    transaction_date DATE,
    region TEXT,
    customer TEXT,
    product TEXT,
    category TEXT,
    units INTEGER,
    unit_price REAL,
    revenue REAL,
    cost REAL
);
