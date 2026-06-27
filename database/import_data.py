import pandas as pd
from db_config import get_connection

# Read CSV
df = pd.read_csv("dataset/segmented_customers.csv")

# Convert date column
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
).dt.date

# Replace NaN with None
df = df.where(pd.notnull(df), None)

# Connect to MySQL
connection = get_connection()

if connection is None:
    exit()

cursor = connection.cursor()

query = """
INSERT INTO customers (
    Customer_ID,
    Gender,
    Age,
    Age_Group,
    Country,
    Nationality,
    Product_Name,
    Category,
    Price,
    Quantity,
    Revenue,
    Profit,
    Rating,
    Order_Hour,
    Shopping_Time,
    Product_View_Count,
    Wishlist_Count,
    Cart_Count,
    Purchase_Frequency,
    Customer_Lifetime_Value,
    Discount_Percent,
    Recommended_Discount,
    Session_Duration_Min,
    Device_Type,
    Order_Date,
    Order_Year,
    Order_Month,
    Order_Day,
    Order_Weekday,
    Revenue_Per_Order,
    Profit_Margin,
    Customer_Value_Score,
    Engagement_Score,
    Shopping_Intent_Score,
    Rating_Category,
    Session_Category,
    Discount_Category,
    Shopping_Period,
    Cluster,
    Customer_Segment_ML
)
VALUES (
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
)
"""

data = [tuple(row) for row in df.values]

cursor.executemany(query, data)

connection.commit()

print(f"✅ {cursor.rowcount} rows inserted successfully.")

cursor.close()
connection.close()