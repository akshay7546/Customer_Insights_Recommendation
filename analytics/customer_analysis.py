import pandas as pd


def total_customers(df):
    return df["Customer_ID"].nunique()


def customer_segments(df):
    segments = (
        df["Customer_Segment_ML"]
        .value_counts()
        .reset_index()
    )
    segments.columns = [
        "Segment",
        "Customers"
    ]
    return segments


def customers_by_country(df):
    country = (
        df.groupby("Country")
        .size()
        .reset_index(name="Customers")
        .sort_values(
            by="Customers",
            ascending=False
        )
    )
    return country


def average_customer_value(df):
    return round(
        df["Customer_Lifetime_Value"].mean(),
        2
    )


def top_customers(df, n=10):
    top = (
        df[
            [
                "Customer_ID",
                "Country",
                "Customer_Lifetime_Value",
                "Revenue"
            ]
        ]
        .sort_values(
            by="Customer_Lifetime_Value",
            ascending=False
        )
        .head(n)
    )
    return top


def shopping_behavior(df):
    shopping = (
        df["Shopping_Period"]
        .value_counts()
        .reset_index()
    )
    shopping.columns = [
        "Shopping_Time",
        "Customers"
    ]
    return shopping


def device_usage(df):
    device = (
        df["Device_Type"]
        .value_counts()
        .reset_index()
    )
    device.columns = [
        "Device",
        "Users"
    ]
    return device