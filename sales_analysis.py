# =====================================
# 1. Import Libraries
# =====================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For better visuals
sns.set(style="whitegrid")

# =====================================
# 2. Load Dataset
# =====================================

# Replace with your dataset file
df = pd.read_csv("sales_data.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Info")
print(df.info())

# =====================================
# 3. Data Cleaning
# =====================================

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.dropna()

# Ensure numeric columns
df['Sales'] = pd.to_numeric(df['Sales'])
df['Profit'] = pd.to_numeric(df['Profit'])
df['Quantity'] = pd.to_numeric(df['Quantity'])

print("\nCleaned Dataset Shape:", df.shape)

# =====================================
# 4. KPI Calculations
# =====================================

total_revenue = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_quantity = df['Quantity'].sum()
avg_order_value = total_revenue / total_orders

print("\n===== BUSINESS KPIs =====")
print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value:", avg_order_value)

# =====================================
# 5. Revenue Trend Analysis
# =====================================

df['Month'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# =====================================
# 6. Top 10 Selling Products
# =====================================

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 Selling Products")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()

# =====================================
# 7. Category Performance
# =====================================

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,6))
category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Category")
plt.ylabel("")
plt.show()

# =====================================
# 8. Regional Sales Performance
# =====================================

region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,6))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="coolwarm")
plt.title("Regional Sales Performance")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()

# =====================================
# 9. Profit by Category
# =====================================

profit_category = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,6))
sns.barplot(x=profit_category.index, y=profit_category.values, palette="magma")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# =====================================
# 10. Top 5 Regions by Profit
# =====================================

top_regions_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,6))
sns.barplot(x=top_regions_profit.index, y=top_regions_profit.values)
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.show()

# =====================================
# 11. Export Analysis Results
# =====================================

summary = {
    "Total Revenue": total_revenue,
    "Total Profit": total_profit,
    "Total Orders": total_orders,
    "Total Quantity Sold": total_quantity,
    "Average Order Value": avg_order_value
}

summary_df = pd.DataFrame(summary, index=["Business Summary"])

summary_df.to_csv("sales_summary_report.csv")

print("\nAnalysis Completed Successfully")
