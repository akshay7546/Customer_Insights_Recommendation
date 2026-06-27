import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def train_churn_model(df):
    """
    Train a simple churn prediction model.
    """

    # Create a churn label
    # Customers with low purchase frequency are assumed to be churned
    df["Churn"] = (
        df["Purchase_Frequency"] <= 1
    ).astype(int)

    features = [
        "Age",
        "Revenue",
        "Profit",
        "Rating",
        "Purchase_Frequency",
        "Customer_Lifetime_Value",
        "Discount_Percent",
        "Session_Duration_Min",
        "Customer_Value_Score",
        "Engagement_Score",
        "Shopping_Intent_Score"
    ]

    X = df[features].fillna(0)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    return model, accuracy


def predict_churn(model, customer_data):
    """
    Predict churn for new customer data.
    """
    prediction = model.predict(customer_data)

    if prediction[0] == 1:
        return "Likely to Churn"

    return "Not Likely to Churn"