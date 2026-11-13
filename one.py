import os
import matplotlib.pyplot as plt
import pandas as pd


def load_and_clean_data(filename="sales.csv"):
    """Reads the CSV file, validates rows, and removes duplicates/invalid entries."""
    if not os.path.exists(filename):
        print(f"Error: '{filename}' not found.")
        return None

    # Read all data as strings first to catch invalid values cleanly
    raw_df = pd.read_csv(filename, dtype=str)

    # Strip whitespace from column names and string values
    raw_df.columns = raw_df.columns.str.strip()
    for col in raw_df.columns:
        raw_df[col] = raw_df[col].str.strip()

    valid_rows = []
    seen_rows = set()

    for idx, row in raw_df.iterrows():
        row_num = idx + 1
        row_tuple = tuple(row)

        # Check for exact duplicate rows
        if row_tuple in seen_rows:
            print(f"Row {row_num} skipped: duplicate row")
            continue

        # Validate Quantity
        try:
            qty = int(row["Quantity"])
            if qty < 0:
                raise ValueError
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: invalid Quantity '{row['Quantity']}'")
            continue

        # Validate Amount
        try:
            amt = float(row["Amount"])
            if amt < 0:
                raise ValueError
        except (ValueError, TypeError):
            print(f"Row {row_num} skipped: invalid Amount '{row['Amount']}'")
            continue

        seen_rows.add(row_tuple)
        valid_rows.append({
            "Date": row["Date"],
            "Product": row["Product"],
            "Region": row["Region"],
            "Quantity": qty,
            "Amount": int(amt) if amt.is_integer() else amt,
        })

    return pd.DataFrame(valid_rows)


def show_summary(df):
    """Displays overall summary (Matches Test Cases 1, 2, and 3)."""
    if df is None or df.empty:
        print("No valid data available.")
        return

    total_revenue = df["Amount"].sum()
    transactions = len(df)
    units_sold = df["Quantity"].sum()

    # Find top-selling product by revenue
    product_sales = df.groupby("Product")["Amount"].sum()
    top_product = product_sales.idxmax()

    print(
        f"Total Revenue: {total_revenue} | Transactions: {transactions} | Units"
        f" sold: {units_sold}"
    )
    print(f"Top product: {top_product}")


def group_and_visualize(df):
    """Groups by Product & Region, displays top 5 products, and plots charts (Matches Test Case 4)."""
    if df is None or df.empty:
        print("No valid data available.")
        return

    # 1. Product-wise sales (sorted descending for Top 5)
    product_sales = (
        df.groupby("Product", sort=False)["Amount"]
        .sum()
        .sort_values(ascending=False)
    )
    product_str = " | ".join(
        [f"{prod}: {val}" for prod, val in product_sales.items()]
    )
    print(product_str)

    # 2. Region-wise sales
    region_sales = df.groupby("Region", sort=False)["Amount"].sum()
    region_str = " | ".join(
        [f"{reg}: {val}" for reg, val in region_sales.items()]
    )
    print(region_str)

    # 3. Top 5 selling products
    print("\n--- Top 5 Selling Products ---")
    top_5 = product_sales.head(5)
    for rank, (prod, val) in enumerate(top_5.items(), start=1):
        print(f"{rank}. {prod}: {val}")

    # 4. Plot two Matplotlib charts (Bar chart & Line chart)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Chart 1: Bar Chart for Region-wise Sales
    axes[0].bar(
        region_sales.index,
        region_sales.values,
        color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"],
    )
    axes[0].set_title("Region-wise Sales")
    axes[0].set_xlabel("Region")
    axes[0].set_ylabel("Total Revenue")

    # Chart 2: Line Chart for Date-wise Sales Trend
    daily_sales = df.groupby("Date")["Amount"].sum()
    axes[1].plot(
        daily_sales.index,
        daily_sales.values,
        marker="o",
        linestyle="-",
        color="#DD8452",
    )
    axes[1].set_title("Daily Sales Trend")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Total Revenue")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    print("Bar chart 'Region-wise Sales' displayed")
    plt.show()


def main():
    df = load_and_clean_data("sales.csv")
    if df is None:
        return

    while True:
        print("\n--- Sales Data Analyzer Menu ---")
        print("1. Summary")
        print("2. Group by Product & Region (with Charts)")
        print("3. Exit")
        choice = input("Enter menu option (1/2/3): ").strip()

        if choice == "1":
            show_summary(df)
        elif choice == "2":
            group_and_visualize(df)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()