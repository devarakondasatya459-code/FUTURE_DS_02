
---

## **Task 2 – Customer Retention & Churn Analysis (`FUTURE_DS_02/README.md`)**

```markdown
# FUTURE_DS_02: Customer Retention & Churn Analysis

## Objective
Analyze customer data to understand churn, calculate customer lifetime value, and perform cohort retention analysis.

## Dataset
The dataset is located in `data/customer_data.csv` and includes:
- `Customer ID` – Unique customer identifier
- `Signup Date` – Date the customer signed up
- `Last Activity Date` – Last active date
- `Subscription Type` – Plan type (Monthly/Yearly)
- `Plan Amount` – Subscription amount
- `Churned` – Whether customer churned (Yes/No)
- `Number of Logins` – Total logins
- `Support Tickets` – Support interactions
- `Region` – Customer region

## Steps Taken
1. Load and clean the dataset (convert dates, map churn to numeric)
2. Calculate key metrics:
   - Total Customers
   - Churned Customers
   - Churn Rate
   - Average Customer Lifetime
   - Approximate Customer Lifetime Value (CLV)
3. Cohort retention analysis:
   - Group customers by signup month and activity month
   - Calculate retention percentages
4. Visualize insights:
   - Churn vs Active pie chart
   - Customer lifetime distribution
   - Plan amount vs churn
   - Cohort retention heatmap
5. Export summary CSV to `outputs/customer_summary_report.csv`

## Tools & Libraries
- Python: `pandas`, `numpy`, `matplotlib`, `seaborn`

## How to Run
```bash
python scripts/retention_analysis.py
