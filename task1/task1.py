import pandas as pd

# 1. LOAD THE DATASET
df = pd.read_csv('train_and_test2.csv')

print("--- BEFORE CLEANING ---")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print(f"\nDuplicates: {df.duplicated().sum()}")

# 2. DROP DUPLICATES
df = df.drop_duplicates()

# 3. FILL MISSING NUMERIC DATA WITH MEDIAN
num_cols = df.select_dtypes(include=['number']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# 4. SAVE CLEANED CSV
df.to_csv('cleaned_train_and_test2.csv', index=False)
print("\nSUCCESS! Task 1 complete. Saved as 'cleaned_train_and_test2.csv'")
