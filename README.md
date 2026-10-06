# Financial Performance Dashboard

I analyzed 1,000 real company transactions from 2025 with Python and SQL, then rebuilt the results as dashboards in both Tableau and Power BI.

## Key Findings

1. **Services make the money. Technology makes the revenue look big.** Services brought in $15.52M (58.3% of revenue) at a 47.8% gross margin. Technology did $11.09M at 29.9%. The split is stark at the product level: Consulting ran a 55.0% margin on $5.40M, while Cloud Software was the biggest product by revenue ($5.59M) and the thinnest by margin (28.2%). The highest-revenue product is the least profitable one.

2. **April was the worst month, and it was not about volume.** April did $1.49M across 74 transactions. Deal count was normal. The problem was deal size: the average April transaction was $20,095, against roughly $27,000 in a typical month. Smaller deals, not fewer deals.

3. **No customer concentration risk.** The top 10 customers account for $5.42M, just 20.4% of revenue. The biggest, Customer 020, is $789K (3.0%). With 80 customers and nobody above 3%, losing any single account does not move the needle.

4. **Regions are balanced, so product mix is the lever.** Southwest leads at $6.06M (22.8%), Midwest trails at $4.20M (15.8%), but gross margins sit in a tight 39.6% to 41.3% band everywhere. Geography is not the margin story. Selling more Consulting and Implementation (48-55% margins) instead of Cloud Software (28.2%) is.

## Tools

- Python (pandas) for the analysis
- SQLite for the schema and queries
- Tableau and Power BI for the dashboards

## Project Structure

```
financial-dashboard/
├── data/
│   ├── financial_analysis.db       # real SQLite database (1,000 rows)
│   └── financial_transactions.csv  # CSV export for Tableau / Power BI
├── python/
│   └── financial_analysis.py       # totals, monthly trend, product/category/region/customer breakdowns
├── sql/
│   ├── schema.sql                  # table definition (matches the real database)
│   └── analysis_queries.sql        # 6 queries: totals, monthly, category, product, region, top customers
├── tableau/
│   └── build_guide.md              # step-by-step Tableau dashboard build
├── powerbi/
│   └── build_guide.md              # step-by-step Power BI dashboard build
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run the Python analysis (reads the SQLite database directly):
   `python3 python/financial_analysis.py`
3. Run the SQL (builds a fresh database from the CSV and runs all six queries):
   ```
   sqlite3 /tmp/financial.db < sql/schema.sql
   sqlite3 /tmp/financial.db ".mode csv" ".import --skip 1 data/financial_transactions.csv financial_transactions"
   sqlite3 /tmp/financial.db < sql/analysis_queries.sql
   ```
4. Build the dashboards: open `data/financial_transactions.csv` in Tableau or Power BI and follow the guide in `tableau/build_guide.md` or `powerbi/build_guide.md`.
