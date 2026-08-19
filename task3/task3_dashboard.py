import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# Create sample dataset (Replace this section with pd.read_csv('your_file.csv') if using real data)
np.random.seed(42)
df = pd.DataFrame(
    {
        "Category": np.random.choice(
            ["Electronics", "Clothing", "Home", "Books"], 100
        ),
        "Sales": np.random.randint(100, 500, 100),
        "Profit": np.random.normal(50, 20, 100),
        "Age": np.random.randint(18, 65, 100),
    }
)

# Initialize 2x2 plot dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    "Task 3: Data Visualization Dashboard", fontsize=16, fontweight="bold"
)

# 1. Bar Chart
sns.barplot(
    ax=axes[0, 0],
    data=df,
    x="Category",
    y="Sales",
    estimator=sum,
    errorbar=None,
    palette="viridis",
)
axes[0, 0].set_title("Total Sales by Category")

# 2. Histogram
sns.histplot(ax=axes[0, 1], data=df, x="Age", bins=10, kde=True, color="teal")
axes[0, 1].set_title("Customer Age Distribution")

# 3. Scatter Plot
sns.scatterplot(
    ax=axes[1, 0], data=df, x="Sales", y="Profit", hue="Category", s=70
)
axes[1, 0].set_title("Sales vs. Profit")

# 4. Pie Chart
category_counts = df["Category"].value_counts()
axes[1, 1].pie(
    category_counts, labels=category_counts.index, autopct="%1.1f%%"
)
axes[1, 1].set_title("Category Distribution")

plt.tight_layout()

# Save dashboard as an image file
plt.savefig("dashboard_output.png", dpi=300, bbox_inches="tight")
print("Dashboard saved successfully as dashboard_output.png!")

# Display the dashboard on screen
plt.show()
