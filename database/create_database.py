import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql"
    )

    cursor = connection.cursor()

    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS customer_insights"
    )

    print("✅ customer_insights database created successfully.")

    cursor.close()
    connection.close()

except mysql.connector.Error as err:
    print(err)