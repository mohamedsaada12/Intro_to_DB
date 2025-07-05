import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host="sql7.freesqldatabase.com",
        port=3306,
        user="sql7788081",
        password="NDZ1llfNGF",
        database="sql7788081"  # connect to the existing DB
    )

    print("Connected to existing database 'sql7788081' successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
