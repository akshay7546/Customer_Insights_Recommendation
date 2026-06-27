from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

# Load Dataset
df = pd.read_csv("dataset/segmented_customers.csv")

# Dashboard Route
@app.route("/")
def dashboard():

    total_customers = df["Customer_ID"].nunique()
    total_revenue = round(df["Revenue"].sum(), 2)
    total_profit = round(df["Profit"].sum(), 2)
    avg_rating = round(df["Rating"].mean(), 2)

    return render_template(
        "dashboard.html",
        total_customers=total_customers,
        total_revenue=total_revenue,
        total_profit=total_profit,
        avg_rating=avg_rating
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

if __name__ == "__main__":
    app.run(debug=True)