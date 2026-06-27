import mysql.connector

# MySQL Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "mysql",
    "database": "customer_insights"
}



# Database Connection Function
def get_connection():
    """
    Create and return a MySQL database connection.
    """

    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            print("Connected to MySQL Database")

        return connection

    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None