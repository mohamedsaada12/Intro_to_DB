import mysql.connector

try:
    connection = mysql.connector.connect(
        host="sql7.freesqldatabase.com",
        user="sql7788081",
        password="NDZ1llfNGF",
        database="sql7788081",
        port=3306
    )

    if connection.is_connected():
        print("✅ Connected to the database!")

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")

        print("📋 Tables in the database:")
        for table in cursor.fetchall():
            print(f"- {table[0]}")

        cursor.close()
        connection.close()

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
