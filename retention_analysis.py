# =====================================
# Customer Retention & Churn Analysis
# =====================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# =====================================
# 1. Load Dataset
# =====================================
df = pd.read_csv("customer_data.csv")

# Convert date columns
df['Signup Date'] = pd.to_datetime(df['Signup Date'])
df['Last Activity Date'] = pd.to_datetime(df['Last Activity Date'])

# Map Churned to numeric
df['Churned'] = df['Churned'].map({'Yes':1, 'No':0})

print("First 5 rows of data:")
print(df.head())

# =====================================
# 2. Calculate KPIs
# =====================================
total_customers = df['Customer ID'].nunique()
churned_customers = df['Churned'].sum()
churn_rate = churned_customers / total_customers * 100

# Customer Lifetime in days
df['Customer_Lifetime'] = (df['Last Activity Date'] - df['Signup Date']).dt.days
avg_lifetime = df['Customer_Lifetime'].mean()

# Average subscription amount
avg_revenue_per_customer = df['Plan Amount'].mean()
CLV = avg_revenue_per_customer * avg_lifetime / 30  # approximate monthly CLV

print("\n===== KEY METRICS =====")
print(f"Total Customers: {total_customers}")
print(f"Churned Customers: {churned_customers}")
print(f"Churn Rate: {churn_rate:.2f}%")
print(f"Average Customer Lifetime (days): {avg_lifetime:.1f}")
print(f"Approx. Customer Lifetime Value: ${CLV:.2f}")

# Save summary to CSV
summary = {
    "Total Customers": total_customers,
    "Churned Customers": churned_customers,
    "Churn Rate (%)": churn_rate,
    "Average Customer Lifetime (days)": avg_lifetime,
    "Approx. CLV": CLV
}

summary_df = pd.DataFrame(summary, index=["Summary"])
summary_df.to_csv("customer_summary_report.csv")
print("Customer summary report saved as 'customer_summary_report.csv'")

# =====================================
# 3. Cohort Retention Analysis
# =====================================
df['Signup_Month'] = df['Signup Date'].dt.to_period('M')
df['Activity_Month'] = df['Last Activity Date'].dt.to_period('M')

cohort_data = df.groupby(['Signup_Month', 'Activity_Month'])['Customer ID'].nunique().unstack()
cohort_size = cohort_data.iloc[:,0]
retention = cohort_data.divide(cohort_size, axis=0)

# =====================================
# 4. Visualizations and Dashboard
# =====================================
plt.figure(figsize=(16,12))
fig, axs = plt.subplots(2, 2, figsize=(16,12))

# 4.1 Churn Rate Pie
labels = ['Active','Churned']
sizes = [total_customers - churned_customers, churned_customers]
axs[0,0].pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#4CAF50','#F44336'])
axs[0,0].set_title("Churn vs Active Customers")

# 4.2 Customer Lifetime Histogram
axs[0,1].hist(df['Customer_Lifetime'], bins=20, color='#2196F3', edgecolor='black')
axs[0,1].set_title("Customer Lifetime Distribution (days)")
axs[0,1].set_xlabel("Lifetime (days)")
axs[0,1].set_ylabel("Number of Customers")

# 4.3 Plan Amount by Churned Status
sns.boxplot(x='Churned', y='Plan Amount', data=df, ax=axs[1,0])
axs[1,0].set_title("Plan Amount vs Churned")
axs[1,0].set_xticklabels(['Active','Churned'])

# 4.4 Cohort Retention Heatmap
sns.heatmap(retention, annot=True, fmt=".0%", cmap="YlGnBu", ax=axs[1,1])
axs[1,1].set_title("Cohort Retention Heatmap")

plt.tight_layout()
plt.savefig("retention_charts.png")
plt.show()

print("Retention charts saved as 'retention_charts.png'")
