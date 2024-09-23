import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server
    connection = mysql.connector.connect(
        host='localhost',         # Replace with your hostname (e.g., 'localhost' or IP address)
        user='root',              # Replace with your MySQL username
        password='5454', # Replace with your MySQL password
        database='data1'    # Optional: Replace with your database name if needed
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute your MySQL query here (e.g., show all databases)
        cursor.execute("SHOW DATABASES;")

        # Fetch all the results
        databases = cursor.fetchall()

        # Print the results
        for db in databases:
            print(db)

    cursor.execute("CREATE DATABASE new1_database;")
    cursor.execute("""
        CREATE TABLE users1 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255)
        );
    """)
    cursor.execute("""
        use new1_database
        INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
    """)
    connection.commit()  # Commit changes to save the insert
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    val = ("John Doe", "john@example.com")
    cursor.execute(sql, val)
    connection.commit()

except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")