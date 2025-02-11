import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Print basic statistics
print("Sales Data Summary:")
print(df.describe())

# Total sales per product
total_sales = df.groupby("Product")["Sales"].sum()
print("\nTotal Sales by Product:")
print(total_sales)

# Total profit per product
total_profit = df.groupby("Product")["Profit"].sum()
print("\nTotal Profit by Product:")
print(total_profit)

# Plot sales trend over time
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['Sales'], marker='o', linestyle='-', color='blue')
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Daily Sales Trend")
plt.xticks(rotation=45)
plt.grid()
plt.savefig("sales_trend.png")
plt.show()
