"""Financial performance analysis on the real company database.

Reads data/financial_analysis.db (SQLite) and prints the core numbers:
totals, monthly trend, product / category / region performance, top customers.
"""
import sqlite3
import pandas as pd

DB = "data/financial_analysis.db"

con = sqlite3.connect(DB)
df = pd.read_sql("SELECT * FROM financial_transactions", con)
con.close()

df["transaction_date"] = pd.to_datetime(df["transaction_date"])
df["gross_profit"] = df["revenue"] - df["cost"]
df["month"] = df["transaction_date"].dt.to_period("M").astype(str)

total_rev = df["revenue"].sum()
total_cost = df["cost"].sum()
total_gp = df["gross_profit"].sum()


def finalize(agg):
    """Add weighted margin and share columns to a grouped aggregation."""
    agg["margin"] = agg["gp"] / agg["revenue"]
    agg["share"] = agg["revenue"] / total_rev
    return agg.drop(columns=["gp"])


print("=== TOTALS ===")
print(f"Transactions : {len(df):,}")
print(f"Revenue      : ${total_rev:,.0f}")
print(f"Cost         : ${total_cost:,.0f}")
print(f"Gross profit : ${total_gp:,.0f}")
print(f"Margin       : {total_gp / total_rev:.1%}")
print(f"Date range   : {df['transaction_date'].min().date()} to {df['transaction_date'].max().date()}")

print("\n=== MONTHLY TREND ===")
monthly = finalize(df.groupby("month").agg(revenue=("revenue", "sum"),
                                            gp=("gross_profit", "sum"),
                                            deals=("transaction_id", "count"),
                                            avg_deal=("revenue", "mean")))
print(monthly.to_string(float_format=lambda x: f"{x:,.1f}"))

print("\n=== BY CATEGORY ===")
cat = finalize(df.groupby("category").agg(revenue=("revenue", "sum"),
                                          gp=("gross_profit", "sum"),
                                          deals=("transaction_id", "count")))
print(cat.to_string(float_format=lambda x: f"{x:,.3f}"))

print("\n=== BY PRODUCT ===")
prod = finalize(df.groupby("product").agg(revenue=("revenue", "sum"),
                                          gp=("gross_profit", "sum"),
                                          deals=("transaction_id", "count")))
print(prod.sort_values("revenue", ascending=False).to_string(float_format=lambda x: f"{x:,.3f}"))

print("\n=== BY REGION ===")
reg = finalize(df.groupby("region").agg(revenue=("revenue", "sum"),
                                        gp=("gross_profit", "sum"),
                                        deals=("transaction_id", "count")))
print(reg.sort_values("revenue", ascending=False).to_string(float_format=lambda x: f"{x:,.3f}"))

print("\n=== TOP 10 CUSTOMERS ===")
top = df.groupby("customer").agg(revenue=("revenue", "sum"),
                                 deals=("transaction_id", "count")).sort_values(
                                     "revenue", ascending=False).head(10)
top["share"] = top["revenue"] / total_rev
print(top.to_string(float_format=lambda x: f"{x:,.3f}"))
print(f"\nTop 10 share of revenue: {top['revenue'].sum() / total_rev:.1%}")
