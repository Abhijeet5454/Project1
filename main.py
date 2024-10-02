#Setup connection with database
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

except Error as e:
    print(f"Error: {e}")

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")


#Display on web
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

#______________________________________________________
#Create tech - name(check for duplicate), blocks, details
def createTech():
    

#______________________________________________________
#Edit tech - details, rearrangement in block, modify/add - blocks, links, 


#______________________________________________________
#Optional - for multiple copy merge tech together

