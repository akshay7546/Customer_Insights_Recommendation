import pandas as pd


def generate_sentiment(df):

    def sentiment(rating):

        if rating >= 4:
            return "Positive"

        elif rating == 3:
            return "Neutral"

        else:
            return "Negative"

    df["Sentiment"] = df["Rating"].apply(sentiment)

    return df


def sentiment_distribution(df):

    sentiment_df = (
        df["Sentiment"]
        .value_counts()
        .reset_index()
    )

    sentiment_df.columns = [
        "Sentiment",
        "Customers"
    ]

    return sentiment_df