import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
data = pd.read_csv("sales.csv")

print("First 5 rows of the dataset:")
print(data.head())

print("\nColumn names in the dataset:")
print(data.columns)

# 2. Group by Product and sum Sales
grouped_sales = data.groupby("Product")["Sales"].sum()

print("\nTotal Sales by Product:")
print(grouped_sales)

# 3. Plot and SAVE the graph (no GUI window)
plt.figure()
grouped_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

# Make layout nice
plt.tight_layout()

# 4. Save as image file
plt.savefig("sales_chart.png")

print("\n✅ Graph saved as 'sales_chart.png' in this folder.")
