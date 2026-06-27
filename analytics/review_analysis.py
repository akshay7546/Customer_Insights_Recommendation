import pandas as pd


def total_reviews(df):
    """
    Total number of reviews/orders.
    """
    return len(df)


def average_rating(df):
    """
    Overall average rating.
    """
    return round(df["Rating"].mean(), 2)


def positive_reviews(df):
    """
    Reviews with rating >= 4.
    """
    positive = df[df["Rating"] >= 4]
    return len(positive)


def neutral_reviews(df):
    """
    Reviews with rating = 3.
    """
    neutral = df[df["Rating"] == 3]
    return len(neutral)


def negative_reviews(df):
    """
    Reviews with rating <= 2.
    """
    negative = df[df["Rating"] <= 2]
    return len(negative)


def review_summary(df):
    """
    Summary of review categories.
    """
    summary = pd.DataFrame({
        "Review_Type": [
            "Positive",
            "Neutral",
            "Negative"
        ],
        "Count": [
            positive_reviews(df),
            neutral_reviews(df),
            negative_reviews(df)
        ]
    })

    return summary


def rating_distribution(df):
    """
    Distribution of ratings.
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
        .sort_values()
        .head(n)
        .reset_index()
    )

    return products


def reviews_by_country(df):
    """
    Number of reviews by country.
    """
    country = (
        df.groupby("Country")
        .size()
        .reset_index(name="Reviews")
        .sort_values(
            by="Reviews",
            ascending=False
        )
    )

    return country