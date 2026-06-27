import pandas as pd

# Load Segmented Dataset
df = pd.read_csv("dataset/segmented_customers.csv")
print("=" * 70)
print("READYNEST BUSINESS INSIGHTS")
print("=" * 70)

# Executive KPIs
print("\nEXECUTIVE KPIs")
print(f"\nTotal Customers : {df['Customer_ID'].nunique()}")
print(f"Total Revenue : ₹{df['Revenue'].sum():,.2f}")
print(f"Total Profit : ₹{df['Profit'].sum():,.2f}")
print(f"Average Rating : {df['Rating'].mean():.2f}")
print(f"Average Order Value : ₹{df['Revenue'].mean():,.2f}")

# Customer Insights
print("\nCUSTOMER INSIGHTS")
print("\nGender Distribution")
print(df["Gender"].value_counts())
print("\nAge Group Distribution")
print(df["Age_Group"].value_counts())

print("\nTop Countries")
print(df["Country"].value_counts().head(10))
print("\nTop Nationalities")
print(df["Nationality"].value_counts().head(10))

# Product Insight
print("\nPRODUCT INSIGHTS")
print("\nTop Selling Products")
print(
    df.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nHighest Revenue Products")
print(
    df.groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nHighest Profit Products")
print(
    df.groupby("Product_Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Rated Products")
print(
    df.groupby("Product_Name")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

# Category Insights
print("\nCATEGORY INSIGHTS")
print("\nRevenue By Category")
print(
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nProfit By Category")
print(
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

# Shopping Behaviour
print("\nSHOPPING BEHAVIOUR")
print("\nShopping Time")
print(df["Shopping_Period"].value_counts())
print("\nDevice Usage")
print(df["Device_Type"].value_counts())
print("\nSession Category")
print(df["Session_Category"].value_counts())

# Discount Insights
print("\nDISCOUNT INSIGHTS")
print("\nAverage Discount")
print(df["Discount_Percent"].mean())
print("\nDiscount Category")
print(df["Discount_Category"].value_counts())

# Segment Insights
print("\nCUSTOMER SEGMENTS")
print(df["Customer_Segment_ML"].value_counts())
print("\nRevenue By Segment")
print(
    df.groupby("Customer_Segment_ML")["Revenue"]
    .sum()
)
print("\nProfit By Segment")
print(
    df.groupby("Customer_Segment_ML")["Profit"]
    .sum()
)

# Country Insights
print("\nCOUNTRY INSIGHTS")
print("\nRevenue By Country")
print(
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)
print("\nOrders By Country")
print(
    df["Country"]
    .value_counts()
)
print("\nAverage Rating By Country")
print(
    df.groupby("Country")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

# Recommendation
print("\nBUSINESS RECOMMENDATIONS")
best_time = df["Shopping_Period"].mode()[0]
best_country = (
    df.groupby("Country")["Revenue"]
    .sum()
    .idxmax()
)

best_product = (
    df.groupby("Product_Name")["Revenue"]
    .sum()
    .idxmax()
)

print(f"\nBest Shopping Time : {best_time}")
print(f"Highest Revenue Country : {best_country}")
print(f"Best Performing Product : {best_product}")
print("\nRecommendation :")
print("- Run campaigns during highest shopping time.")
print("- Focus marketing on highest revenue country.")
print("- Promote highest revenue products.")
print("- Give higher discounts on low selling products.")
print("- Give premium offers to Platinum customers.")
print("\nBusiness Insights Generated Successfully")