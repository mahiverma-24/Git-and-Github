# Sales Data Analyzer

A Python 3 console project that analyses a sales CSV file to find total revenue, best-selling products and region-wise performance using Pandas grouping, and visualises the results with Matplotlib.

## Problem Statement

Analyse a sales CSV file to find total revenue, best-selling products and region-wise performance using grouping, and visualise the results.

- **Language:** Python 3
- **Concepts:** Pandas, CSV, Matplotlib, Grouping
- **CSV columns:** `Date, Product, Region, Quantity, Amount`

## Features

- Reads the CSV with Pandas (works with or without a header row)
- Cleans data: skips invalid rows (bad Date, Quantity or Amount, missing values) with a clear message, and removes duplicate rows
- Uses `groupby()` for product-wise and region-wise sales
- Shows the top 5 selling products
- Plots Matplotlib charts: bar chart (region-wise and product-wise sales) and line chart (daily revenue trend)

## Requirements

- Python 3.8+
- pandas
- matplotlib

```bash
pip install pandas matplotlib
```

## How to Run

```bash
python one.py sales.csv
```

If no file name is given, `sales.csv` in the current folder is used.

### Menu

```
1. Summary
2. Group by Product & Region
3. Top 5 selling products
4. Charts (bar + line)
5. Exit
```

## Approach

1. **Load:** read the CSV as text using Pandas with the fixed column names.
2. **Clean:** validate each row (date, quantity, amount). Invalid rows are skipped and reported by row number. Duplicates are dropped.
3. **Analyse:** use `groupby("Product")` and `groupby("Region")` to total the Amount and Quantity.
4. **Visualise:** draw bar and line charts with Matplotlib and save them as PNG files.

## Test Cases

### Test Case 1: Normal Input

`sales.csv`
```
2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,5000
2026-08-03,Laptop,South,1,50000
```
Menu option 1 (Summary)

**Output:** `Total Revenue: 155000 | Transactions: 3 | Units sold: 13 | Top product: Mouse`

### Test Case 2: Boundary / Minimum Input

`sales.csv` (1 row only)
```
2026-08-01,Mouse,North,1,500
```
Menu option 1 (Summary)

**Output:** `Total Revenue: 500 | Transactions: 1 | Units sold: 1 | Top product: Mouse`

### Test Case 3: Invalid Input

`sales.csv`
```
2026-08-01,Laptop,North,2,100000
2026-08-02,Mouse,South,10,abc
2026-08-03,Laptop,South,1,50000
```

**Output:**
```
Row 2 skipped: invalid Amount 'abc'
Total Revenue: 150000 | Transactions: 2 | ...
```

### Test Case 4: Different Valid Scenario

Same CSV as Test Case 1, Menu option 2 (Group by Product & Region)

**Output:**
```
Product-wise sales: Laptop: 150000 | Mouse: 5000
Region-wise sales:  North: 100000 | South: 55000
Bar chart 'Region-wise Sales' displayed
```

## Project Structure

```
sales-data-analyzer/
├──README.md
├──one.py
├──region_sales.png
└──sales.csv
```
