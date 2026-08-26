import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df = pd.read_csv('customer_data.csv')

# 2. Segment Customers by Age Group
bins = [17, 30, 45, 65]
labels = ['Young Adult (18-30)', 'Middle-Aged (31-45)', 'Senior (46-65)']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 3. Identify Top Customer Groups by Spend
spending_by_age = df.groupby('AgeGroup')['TotalSpend'].sum().reset_index()
print("--- TOTAL SPEND BY AGE GROUP ---")
print(spending_by_age)

# 4. Create Visual Reports
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Age vs Spending
sns.barplot(data=df, x='AgeGroup', y='TotalSpend', ax=axes[0], palette='viridis')
axes[0].set_title('Total Spend by Age Group')

# Plot 2: Location vs Spending
sns.boxplot(data=df, x='Location', y='TotalSpend', ax=axes[1], palette='magma')
axes[1].set_title('Spending Distribution by Location')

plt.tight_layout()
plt.show()
