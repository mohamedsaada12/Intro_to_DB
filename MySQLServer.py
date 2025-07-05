import mysql.connector
from mysql.connector import errorcode

try:
    # 1) Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host="sql7.freesqldatabase.com",
        port=3306,
        user="sql7788081",
        password="NDZ1llfNGF"
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
