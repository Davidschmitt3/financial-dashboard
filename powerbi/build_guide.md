# Power BI Build Guide: Financial Performance Dashboard

Build time: about 1 hour. Data file: `data/financial_transactions.csv` (1,000 rows, Jan-Dec 2025, real company data).

Fields: `transaction_id`, `transaction_date`, `region`, `customer`, `product`, `category`, `units`, `unit_price`, `revenue`, `cost`. Revenue and cost are precomputed per row.

## Step 1: Load and prep (10 min)

1. **Home > Get Data > Text/CSV**, select `financial_transactions.csv`, click **Load**.
2. In **Data view**, check types: `transaction_date` = Date, `units` = Whole Number, `unit_price`/`revenue`/`cost` = Decimal Number.
3. Create two DAX measures (right-click the table > **New measure**):
   - `Gross Profit = SUM(financial_transactions[revenue]) - SUM(financial_transactions[cost])`
   - `Gross Margin = DIVIDE([Gross Profit], SUM(financial_transactions[revenue]))`, then set its format to **Percentage** (1 decimal) in the Measure Tools ribbon.

## Step 2: Build the visuals (30 min)

### Visual 1: "Monthly Trend" (line chart)

1. Insert a **Line chart**. Axis: `transaction_date` (use the auto date hierarchy, drill to **Month**).
2. Y-axis: `SUM(revenue)`. Secondary Y-axis: turn it **On** and add `Gross Margin`.
3. Format the primary axis as currency, secondary as percentage.
4. April 2025 will show as the clear dip.

### Visual 2: "Revenue by Product" (bar chart)

1. Insert a **Clustered bar chart**. Y-axis: `product`, X-axis: `SUM(revenue)`.
2. Sort descending by revenue (click the ... menu > Sort by > revenue).
3. Add `Gross Margin` to the **Color saturation** / conditional formatting of the bars (or use a second small bar chart of margin by product next to it). Cloud Software = lowest margin, Consulting = highest.
4. Turn **Data labels** on.

### Visual 3: "Services vs Technology" (bar chart)

1. Insert a **Clustered column chart**. X-axis: `category`, Y-axis: `SUM(revenue)`.
2. Add `Gross Margin` as data labels via a tooltip or a second series. The margin gap is the story here.
3. Data labels on.

### Visual 4: "Regional Performance" (bar chart)

1. Insert a **Clustered bar chart**. Y-axis: `region`, X-axis: `SUM(revenue)`, sort descending.
2. Data labels on. Margins will look nearly flat across regions.

### Visual 5: "Top 10 Customers" (bar chart)

1. Insert a **Clustered bar chart**. Y-axis: `customer`, X-axis: `SUM(revenue)`.
2. With the visual selected: **Filters pane > customer > Filter type: Top N > Top 10 by SUM(revenue)**.
3. Add `region` to the **Legend** to color by region. Customer 020 leads.

### Visual 6: KPI cards

1. Insert three **Card** visuals: `SUM(revenue)` (currency), `Gross Profit` (currency), `Gross Margin` (percentage).
2. Bump the callout font size up and place them in a row at the top.

## Step 3: Assemble the report (15 min)

1. Page size 1366 x 768 (**View > Page size > Custom**).
2. Layout, top to bottom:
   - **Title text box**: "Financial Performance Dashboard" + "2025 | 1,000 transactions | $26.6M revenue".
   - Row 1: the three KPI cards.
   - Row 2: "Monthly Trend" (wide left) + "Services vs Technology" (right).
   - Row 3: "Revenue by Product" (left) + "Regional Performance" (right).
   - Row 4: "Top 10 Customers" (full width).
3. Add slicers: `category` (dropdown), `region` (dropdown), `transaction_date` (date range slider).
4. Interactivity is on by default (clicking a product filters everything). Check **Format > Edit interactions** if any visual misbehaves.
5. Tidy up: light gray page background, white visual backgrounds, gridlines off on bar charts.

## Step 4: Sanity checks (5 min)

- Cards: Revenue $26,614,088 | Gross Profit $10,744,924 | Gross Margin 40.4%.
- Monthly Trend: April 2025 lowest at $1,487,005.
- Revenue by Product: Cloud Software $5,588,039 at 28.2% margin; Consulting $5,399,693 at 55.0%.
- Services vs Technology: Services $15,524,362 at 47.8% vs Technology $11,089,726 at 29.9%.
- Top 10 Customers: Customer 020 leads at $789,036.
- If anything looks off, re-check the two DAX measures first.
