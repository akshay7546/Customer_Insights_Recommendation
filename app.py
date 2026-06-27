from flask import Flask, render_template
from database.db_config import get_connection
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


# Load Dataset
engine = create_engine(
    "mysql+pymysql://root:mysql@localhost/customer_insights"
)

df = pd.read_sql(
    "SELECT * FROM customers",
    engine
)

# Dashboard Route

@app.route("/")
def dashboard():

    # ==========================
    # Executive KPIs
    # ==========================

    total_customers = df["Customer_ID"].nunique()
    total_revenue = round(df["Revenue"].sum(), 2)
    total_profit = round(df["Profit"].sum(), 2)
    avg_rating = round(df["Rating"].mean(), 2)
    total_orders = len(df)

    # ==========================
    # Top Revenue Products
    # ==========================

    top_products = (
        df.groupby("Product_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    # ==========================
    # Top Rated Products
    # ==========================

    top_rated_products = (
        df.groupby("Product_Name")["Rating"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

    # ==========================
    # Revenue by Country
    # ==========================

    country_sales = (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    # ==========================
    # Orders by Country
    # ==========================

    country_orders = (
        df.groupby("Country")
        .size()
        .reset_index(name="Orders")
    )

    # ==========================
    # Average Rating by Country
    # ==========================

    country_rating = (
        df.groupby("Country")["Rating"]
        .mean()
        .round(2)
        .reset_index()
    )

    # ==========================
    # Customer Segments
    # ==========================

    customer_segments = (
        df["Customer_Segment_ML"]
        .value_counts()
        .reset_index()
    )

    customer_segments.columns = [
        "Segment",
        "Customers"
    ]

    # ==========================
    # Shopping Behaviour
    # ==========================

    shopping_period = (
        df["Shopping_Period"]
        .value_counts()
        .reset_index()
    )

    shopping_period.columns = [
        "Shopping_Time",
        "Customers"
    ]

    # ==========================
    # Device Usage
    # ==========================

    device_usage = (
        df["Device_Type"]
        .value_counts()
        .reset_index()
    )

    device_usage.columns = [
        "Device",
        "Users"
    ]

    # ==========================
    # Revenue by Category
    # ==========================

    category_sales = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    # ==========================
    # Recent Orders
    # ==========================

    recent_orders = (
        df[
            [
                "Customer_ID",
                "Product_Name",
                "Country",
                "Revenue",
                "Rating"
            ]
        ]
        .tail(10)
    )

    # ==========================
    # Monthly Revenue
    # ==========================

    monthly_sales = []

    if "Order_Month" in df.columns:

        monthly_sales = (
            df.groupby("Order_Month")["Revenue"]
            .sum()
            .reset_index()
        )

        monthly_sales = monthly_sales.to_dict(
            orient="records"
        )

    # ==========================
    # Render Dashboard
    # ==========================

    return render_template(

        "dashboard.html",

        total_customers=total_customers,
        total_revenue=total_revenue,
        total_profit=total_profit,
        avg_rating=avg_rating,
        total_orders=total_orders,

        top_products=top_products.to_dict(orient="records"),
        top_rated_products=top_rated_products.to_dict(orient="records"),

        country_sales=country_sales.to_dict(orient="records"),
        country_orders=country_orders.to_dict(orient="records"),
        country_rating=country_rating.to_dict(orient="records"),

        customer_segments=customer_segments.to_dict(orient="records"),

        shopping_period=shopping_period.to_dict(orient="records"),

        device_usage=device_usage.to_dict(orient="records"),

        category_sales=category_sales.to_dict(orient="records"),

        recent_orders=recent_orders.to_dict(orient="records"),

        monthly_sales=monthly_sales
    )

# Customer Page

@app.route("/customers")
def customers():
    return render_template("customers.html")


# Product Page

@app.route("/products")
def products():
    return render_template("products.html")


# Sales Page

@app.route("/sales")
def sales():
    return render_template("sales.html")


# Recommendation Page

@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")


# Business Insights

@app.route("/insights")
def insights():
    return render_template("insights.html")

# Run App

if __name__ == "__main__":
    app.run(debug=True)
