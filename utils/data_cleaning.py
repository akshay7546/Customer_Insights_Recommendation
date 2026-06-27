import pandas as pd

# Load Dataset
df = pd.read_csv("dataset/raw_data.csv")

print("=" * 50)
print("Dataset Shape:", df.shape)
print("=" * 50)

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Check Duplicate Rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Handle Missing Values

# Numerical Columns
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Categorical Columns
cat_cols = df.select_dtypes(include=['object']).columns

for col in cat_cols:
    df[col] = df[col].fillna("Unknown")

# Convert Date Column
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Final Check
print("\nMissing Values After Cleaning:")
print(df.isnull().sum().sum())

print("\nFinal Shape:", df.shape)

# Save Cleaned Dataset
df.to_csv("dataset/cleaned_data.csv", index=False)

print("\n✅ Cleaned dataset saved as:")
print("dataset/cleaned_data.csv")
