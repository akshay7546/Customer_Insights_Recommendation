from db_config import get_connection

connection = get_connection()

if connection is None:
    exit()

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS customers (

    Customer_ID VARCHAR(20) PRIMARY KEY,
    Gender VARCHAR(20),
    Age INT,
    Age_Group VARCHAR(50),
    Country VARCHAR(100),
    Nationality VARCHAR(100),
    Product_Name VARCHAR(255),
    Category VARCHAR(100),
    Price DECIMAL(10,2),
    Quantity INT,
    Revenue DECIMAL(15,2),
    Profit DECIMAL(15,2),
    Rating FLOAT,
    Order_Hour INT,
    Shopping_Time VARCHAR(50),
    Product_View_Count INT,
    Wishlist_Count INT,
    Cart_Count INT,
    Purchase_Frequency INT,
    Customer_Lifetime_Value DECIMAL(15,2),
    Discount_Percent FLOAT,
    Recommended_Discount FLOAT,
    Session_Duration_Min FLOAT,
    Device_Type VARCHAR(50),
    Order_Date DATE,
    Order_Year INT,
    Order_Month INT,
    Order_Day INT,
    Order_Weekday VARCHAR(30),
    Revenue_Per_Order DECIMAL(15,2),
    Profit_Margin FLOAT,
    Customer_Value_Score FLOAT,
    Engagement_Score FLOAT,
    Shopping_Intent_Score FLOAT,
    Rating_Category VARCHAR(50),
    Session_Category VARCHAR(50),
    Discount_Category VARCHAR(50),
    Shopping_Period VARCHAR(50),
    Cluster INT,
    Customer_Segment_ML VARCHAR(50)

)

""")

connection.commit()

print("✅ customers table created successfully.")

cursor.close()
connection.close()