import pandas as pd
from sklearn.linear_model import LinearRegression


def forecast_sales(df):

    monthly_sales = (
        df.groupby("Order_Month")["Revenue"]
        .sum()
        .reset_index()
    )

    X = monthly_sales[["Order_Month"]]
    y = monthly_sales["Revenue"]

    model = LinearRegression()
    model.fit(X, y)

    future_months = pd.DataFrame({
        "Order_Month": [13, 14, 15]
    })

    predictions = model.predict(future_months)

    forecast_df = pd.DataFrame({
        "Future_Month": [13, 14, 15],
        "Predicted_Revenue": predictions
    })

    return forecast_df