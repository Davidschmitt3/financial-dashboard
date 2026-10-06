# Tableau Build Guide: Financial Performance Dashboard

Build time: about 1 hour. Data file: `data/financial_transactions.csv` (1,000 rows, Jan-Dec 2025, real company data).

Fields: `transaction_id`, `transaction_date`, `region`, `customer`, `product`, `category`, `units`, `unit_price`, `revenue`, `cost`. Revenue and cost are precomputed per row, so you only need two calculated fields.

## Step 1: Connect and prep (10 min)

1. Open Tableau Desktop and click **Connect > To a File > Text File**. Select `financial_transactions.csv`.
2. Check the data grid and fix types if needed:
   - `transaction_date` -> Date
   - `units` -> Whole Number
   - `unit_price`, `revenue`, `cost` -> Decimal Number
3. Create two calculated fields (right-click the Data pane > **Create Calculated Field**):
   - `Gross Profit` = `SUM([revenue]) - SUM([cost])`
   - `Gross Margin` = `(SUM([revenue]) - SUM([cost])) / SUM([revenue])`, then right-click it > **Default Properties > Number Format > Percentage** (1 decimal).

## Step 2: Build the sheets (30 min)

### Sheet 1: "Monthly Trend" (line chart)

1. Drag `transaction_date` to **Columns**, right-click the pill and pick **Month** (continuous, blue).
2. Drag `revenue` (as SUM) to **Rows**. Mark type **Line**.
3. Drag `Gross Margin` to **Rows**, right-click the pill > **Dual Axis**. Leave the axes unsynchronized so margin keeps its own scale.
4. Format left axis as Currency, right axis as Percentage.
5. Name it "Monthly Trend". April 2025 will show as the clear dip.

### Sheet 2: "Revenue by Product" (bar chart)

1. Drag `product` to **Rows**, `revenue` (SUM) to **Columns**.
2. Sort `product` descending by SUM(revenue).
3. Drag `Gross Margin` to **Color**, Orange-Blue Diverging palette, 5 stepped colors. Cloud Software will light up as the low-margin outlier; Consulting as the high-margin one.
4. Add `revenue` labels, formatted as currency.
5. Name it "Revenue by Product".

### Sheet 3: "Services vs Technology" (bar chart)

1. Drag `category` to **Columns**, `revenue` (SUM) to **Rows**.
2. Drag `Gross Margin` to **Color** (same diverging palette).
3. Add data labels. The margin gap between the two bars is the story of this dataset.
4. Name it "Services vs Technology".

### Sheet 4: "Regional Performance" (bar chart)

1. Drag `region` to **Rows**, `revenue` (SUM) to **Columns**, sort descending.
2. Drag `Gross Margin` to **Color**. Margins will look nearly identical across regions, which is itself the point.
3. Name it "Regional Performance".

### Sheet 5: "Top 10 Customers" (bar chart)

1. Drag `customer` to **Rows**, `revenue` (SUM) to **Columns**, sort descending.
2. Drag `customer` to **Filters** > **Top** tab > By Field > Top 10 by SUM(revenue).
3. Drag `region` to **Color** to show where the big accounts sit.
4. Name it "Top 10 Customers". Customer 020 will sit clearly on top.

### Sheet 6: "KPIs" (big numbers)

1. New sheet. Drag `revenue` (SUM) to **Text**, format as currency, ~24pt bold.
2. Duplicate the sheet twice; swap the measure for `Gross Profit` (currency) and `Gross Margin` (percentage).
3. Name it "KPIs".

## Step 3: Assemble the dashboard (15 min)

1. New dashboard, size **Automatic** or 1366 x 768.
2. Layout, top to bottom:
   - **Title**: "Financial Performance Dashboard" + subtitle "2025 | 1,000 transactions | $26.6M revenue".
   - Row 1: "KPIs".
   - Row 2: "Monthly Trend" (wide left) + "Services vs Technology" (right).
   - Row 3: "Revenue by Product" (left) + "Regional Performance" (right).
   - Row 4: "Top 10 Customers" (full width).
3. Add dashboard filters (right-click each sheet > **Filters**):
   - `category` as multi-select dropdown.
   - `region` as multi-select dropdown.
   - `transaction_date` as a month range slider.
4. Interactivity: **Dashboard > Actions > Add Action > Highlight**. Source = "Revenue by Product", targets = the rest, field = `product`.
5. Tidy up: **Format > Dashboard**, light gray background (#F5F5F5), white sheet backgrounds, gridlines off on bar charts.

## Step 4: Sanity checks (5 min)

- KPIs: Revenue $26,614,088 | Gross Profit $10,744,924 | Gross Margin 40.4%.
- Monthly Trend: April 2025 is the lowest point at $1,487,005.
- Revenue by Product: Cloud Software on top at $5,588,039 with the worst margin color (28.2%); Consulting at $5,399,693 with the best (55.0%).
- Services vs Technology: Services $15,524,362 at 47.8% vs Technology $11,089,726 at 29.9%.
- Top 10 Customers: Customer 020 leads at $789,036.
- If anything looks off, re-check the two calculated fields first.
