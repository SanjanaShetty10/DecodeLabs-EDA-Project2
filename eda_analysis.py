import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel dataset
df = pd.read_excel("dataset.xlsx")

# Display basic information
print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATASET INFORMATION ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- BASIC STATISTICS ---")
print(df.describe(include="all"))

# Save the summary
df.describe(include="all").to_csv("eda_summary.csv")

print("\nEDA summary saved as eda_summary.csv")
# Count orders for each product
product_counts = df["Product"].value_counts()

# Create a bar chart
plt.figure(figsize=(10, 6))
product_counts.plot(kind="bar")

plt.title("Number of Orders by Product")
plt.xlabel("Product")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("product_orders.png")
plt.show()

print("Product chart saved as product_orders.png")
# Count orders by status
status_counts = df["OrderStatus"].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 5))
status_counts.plot(kind="bar")

plt.title("Number of Orders by Status")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("order_status.png")
plt.show()

print("Order status chart saved as order_status.png")
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Group total sales by month
monthly_sales = (
    df.dropna(subset=["Date"])
      .set_index("Date")
      .resample("MS")["TotalPrice"]
      .sum()
)

# Create a monthly sales chart
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("monthly_sales.png")
plt.show()

print("Monthly sales chart saved as monthly_sales.png")
# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Group total sales by month
monthly_sales = (
    df.dropna(subset=["Date"])
      .set_index("Date")
      .resample("MS")["TotalPrice"]
      .sum()
)

# Create a monthly sales chart
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig("monthly_sales.png")
plt.show()

print("Monthly sales chart saved as monthly_sales.png")
