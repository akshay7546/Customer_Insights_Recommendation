import pandas as pd


def average_rating(df):
    """
    Calculate overall average rating.
    """
    return round(df["Rating"].mean(), 2)


def rating_distribution(df):
    """
    Count of each rating value.
    """
    ratings = (
        df["Rating"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    ratings.columns = [
        "Rating",
        "Customers"
    ]

    return ratings


def rating_by_country(df):
    """
    Average rating by country.
    """
    country_rating = (
        df.groupby("Country")["Rating"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .reset_index()
    )

    return country_rating


def rating_by_category(df):
    """
    Average rating by product category.
    """
    category_rating = (
        df.groupby("Category")["Rating"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .reset_index()
    )

    return category_rating


def top_rated_products(df, n=10):
    """
    Top rated products.
    """
    products = (
        df.groupby("Product_Name")["Rating"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

    return products


def low_rated_products(df, n=10):
    """
    Lowest rated products.
    """
    products = (
        df.groupby("Product_Name")["Rating"]
        .mean()
        .round(2)
        .sort_values(ascending=True)
        .head(n)
        .reset_index()
    )

    return products


def rating_category_distribution(df):
    """
    Distribution of rating categories.
    """
    distribution = (
        df["Rating_Category"]
        .value_counts()
        .reset_index()
    )

    distribution.columns = [
        "Rating_Category",
        "Customers"
    ]

    return distribution