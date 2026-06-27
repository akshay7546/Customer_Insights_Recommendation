import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql",
            database="customer_insights"
        )

        print("Connected to MySQL Database")
        return connection

    except mysql.connector.Error as err:
        print("Database Connection Error:")
        print(err)
        return None