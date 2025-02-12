import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
csv_file = "sales_data.csv"
df_csv = pd.read_csv(csv_file)
df_csv["Revenue"] = df_csv["Quantity"] * df_csv["Price"]

print("\nCSV Data Preview:\n", df_csv.head())

# Connect to SQLite database
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Load data from SQL
query = "SELECT date, product, quantity, price, (quantity * price) AS revenue FROM sales"
df_sql = pd.read_sql(query, conn)

# Convert date column to datetime
df_sql["date"] = pd.to_datetime(df_sql["date"])

# Total Sales by Product
total_sales = df_sql.groupby("product")["revenue"].sum()
print("\nTotal Sales by Product (SQL):\n", total_sales)

# Total Quantity Sold by Product
total_quantity = df_sql.groupby("product")["quantity"].sum()
print("\nTotal Quantity Sold by Product (SQL):\n", total_quantity)

# Sales Trend Over Time
plt.figure(figsize=(8,5))
plt.plot(df_sql["date"], df_sql["revenue"], marker='o', linestyle='-', color='blue', label="Revenue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Daily Sales Trend")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.savefig("sales_trend.png")  # Save the plot
plt.show()

# Close connection
conn.close()
