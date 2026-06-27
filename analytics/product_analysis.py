import pandas as pd


def total_products(df):
    return df["Product_Name"].nunique()


def top_revenue_products(df, n=10):
    products = (
        df.groupby("Product_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return products


def top_rated_products(df, n=10):
    products = (
        df.groupby("Product_Name")["Rating"]
        .mean()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return products


def category_revenue(df):
    category = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return category


def category_profit(df):
    category = (
        df.groupby("Category")["Profit"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return category


def average_product_rating(df):
    return round(df["Rating"].mean(), 2)


def most_viewed_products(df, n=10):
    products = (
        df.groupby("Product_Name")["Product_View_Count"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return products


def most_wishlisted_products(df, n=10):
    products = (
        df.groupby("Product_Name")["Wishlist_Count"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return products


def most_added_to_cart(df, n=10):
    products = (
        df.groupby("Product_Name")["Cart_Count"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return products