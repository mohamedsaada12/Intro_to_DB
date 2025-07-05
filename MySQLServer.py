import os
import mysql.connector
from mysql.connector import errorcode

# Read connection parameters from environment, or use defaults
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")

try:
    # 1) Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS
    )

    cursor = connection.cursor()

    # 2) Create the database alxbookstore if it doesn’t already exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    print("Database 'alxbookstore' created successfully!")

except mysql.connector.Error as err:
    # 3) Exception handling
    print("Error:", err)

finally:
    # 4) Cleanly close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
