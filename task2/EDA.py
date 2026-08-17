import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load Titanic dataset directly from seaborn
print("--- Step 1: Loading Data ---")
df = sns.load_dataset("titanic")
print(df.head())

# 2. Descriptive Statistics
print("\n--- Step 2: Summary Statistics ---")
print(df.info())
print("\n", df.describe())

# 3. Analyze Trends & Relationships (Charts will open in popup windows)
print("\n--- Step 3: Generating Visualizations ---")

# Chart A: Survival by Gender
sns.barplot(data=df, x="sex", y="survived")
plt.title("Survival Rate by Gender")
plt.show()  # Close the pop-up window to continue script execution

# Chart B: Survival by Class
sns.barplot(data=df, x="class", y="survived")
plt.title("Survival Rate by Passenger Class")
plt.show()  # Close the pop-up window to continue script execution

# 4. Outlier Detection
sns.boxplot(x=df["fare"])
plt.title("Ticket Fare Outliers")
plt.show()

print("\nTask 2 Complete!")
