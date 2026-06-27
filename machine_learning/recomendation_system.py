import pandas as pd

# Load Segmented Dataset
df = pd.read_csv("dataset/segmented_customers.csv")
print("=" * 60)
print("Product Recommendation System Started")
print("=" * 60)

# Top Selling Products
top_selling = (
    df.groupby("Product_Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Selling Products")
print(top_selling)

# Most Viewed Products
most_viewed = (
    df.groupby("Product_Name")["Product_View_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Most Viewed Products")
print(most_viewed)

# Most Wishlisted Products
wishlist_products = (
    df.groupby("Product_Name")["Wishlist_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Wishlisted Products")
print(wishlist_products)

# Most Added To Cart
cart_products = (
    df.groupby("Product_Name")["Cart_Count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Added To Cart Products")
print(cart_products)

# Highest Revenue Products
revenue_products = (
    df.groupby("Product_Name")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop Revenue Products")
print(revenue_products)

# Best Rated Products
rating_products = (
    df.groupby("Product_Name")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nBest Rated Products")
print(rating_products)

# Country Wise Recommendations
country_recommendation = (
    df.groupby(["Country", "Product_Name"])["Revenue"]
    .sum()
    .reset_index()
)

country_recommendation = (
    country_recommendation
    .sort_values(["Country", "Revenue"], ascending=[True, False])
)

country_recommendation = (
    country_recommendation
    .groupby("Country")
    .head(5)
)

print("\nCountry Wise Recommended Products")
print(country_recommendation)

# Customer Segment Recommendation
segment_recommendation = (
    df.groupby(
        ["Customer_Segment_ML", "Product_Name"]
    )["Revenue"]
    .sum()
    .reset_index()
)

segment_recommendation = (
    segment_recommendation
    .sort_values(
        ["Customer_Segment_ML", "Revenue"],
        ascending=[True, False]
    )
)

segment_recommendation = (
    segment_recommendation
    .groupby("Customer_Segment_ML")
    .head(5)
)

print("\nSegment Wise Recommended Products")
print(segment_recommendation)

# Save Recommendation Dataset
recommendation = pd.concat(
    [
        revenue_products.rename("Revenue"),
        most_viewed.rename("Views"),
        wishlist_products.rename("Wishlist"),
        cart_products.rename("Cart")
    ],
    axis=1
)

recommendation.reset_index(inplace=True)

recommendation.rename(
    columns={
        "index": "Product_Name"
    },
    inplace=True
)

recommendation.to_csv(
    "dataset/recommended_products.csv",
    index=False
)

print("\nRecommendation Dataset Saved")
print("dataset/recommended_products.csv")

print("\nRecommendation System Completed Successfully")