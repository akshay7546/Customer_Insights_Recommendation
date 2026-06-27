import pandas as pd

# Load Cleaned Dataset
df = pd.read_csv("dataset/cleaned_data.csv")

print("=" * 50)
print("Starting Feature Engineering")
print("=" * 50)

# Date Conversion
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Date Features
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_Day"] = df["Order_Date"].dt.day
df["Order_Weekday"] = df["Order_Date"].dt.day_name()

# Revenue Features
df["Revenue_Per_Order"] = (
    df["Revenue"] / df["Quantity"]
).round(2)

# Profit Features
df["Profit_Margin"] = (
    (df["Profit"] / df["Revenue"]) * 100
).round(2)

# Customer Value Score
df["Customer_Value_Score"] = (
    df["Customer_Lifetime_Value"] *
    df["Purchase_Frequency"]
)

# Customer Engagement Score
df["Engagement_Score"] = (
    df["Product_View_Count"] +
    (df["Wishlist_Count"] * 2) +
    (df["Cart_Count"] * 3)
)

# Shopping Intent Score
df["Shopping_Intent_Score"] = (
    df["Wishlist_Count"] +
    df["Cart_Count"] +
    df["Purchase_Frequency"]
)

# Rating Category
df["Rating_Category"] = df["Rating"].apply(
    lambda x: "Excellent"
    if x >= 4
    else "Average"
    if x >= 3
    else "Poor"
)

# Session Category
df["Session_Category"] = pd.cut(
    df["Session_Duration_Min"],
    bins=[0, 15, 30, 60, 120],
    labels=[
        "Very Low",
        "Low",
        "Medium",
        "High"
    ]
)

# Discount Category
df["Discount_Category"] = pd.cut(
    df["Discount_Percent"],
    bins=[-1, 5, 15, 25, 50],
    labels=[
        "Low",
        "Medium",
        "High",
        "Very High"
    ]
)

# Shopping Time Category
def shopping_period(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 18:
        return "Afternoon"
    elif 18 <= hour < 22:
        return "Evening"
    else:
        return "Night"

df["Shopping_Period"] = df["Order_Hour"].apply(
    shopping_period
)

# EDA Summary
print("\nDataset Shape:")
print(df.shape)

print("\nTotal Revenue:")
print(round(df["Revenue"].sum(), 2))

print("\nTotal Profit:")
print(round(df["Profit"].sum(), 2))

print("\nAverage Rating:")
print(round(df["Rating"].mean(), 2))

print("\nTop Categories:")
print(df["Category"].value_counts().head())

print("\nTop Countries:")
print(df["Country"].value_counts().head())

print("\nGender Distribution:")
print(df["Gender"].value_counts())

print("\nShopping Time Distribution:")
print(df["Shopping_Period"].value_counts())

# Save Processed Dataset
df.to_csv(
    "dataset/processed_data.csv",
    index=False
)

print("\nProcessed Dataset Saved")
print("dataset/processed_data.csv")


