import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password'
    )
    cursor = connection.cursor()

    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

except mysql.connector.Error as err:
    print(f"Error: Could not connect to the MySQL Server.\n{err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

