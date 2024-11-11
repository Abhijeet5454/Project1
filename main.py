#%% Libraries
from pymongo import MongoClient
import mysql.connector
from flask import Flask, render_template, request, jsonify

#%% Setup connection with MongoDB database
# Connection URL
client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
vmainDB = client.mainDB

vmainCol = vmainDB.maincollection
vinfoCol = vmainDB.infocollection

#%% Setup connection with MySQL database
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

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


#%% Display on web
app = Flask(__name__)

# Route to handle the form page
@app.route('/')
def index():
    return render_template('homePage.html')

@app.route('/newTechEntry')
def index():
    return render_template('newTechEntry.html')

# Route to handle the data submission
@app.route('/verifyDuplicate', methods=['POST'])
def submit_data():
    # Get data from the form
    newTechName = request.get_json()

    # response = verify_duplicate(newTechName)
    response = newTechName + "is entered"
    # Return result to the HTML page
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


#%% Functions

def verify_duplicate(text):
    return True

def verify_techName():
    return True

def create_techName(): #Temporary techname with ID with verify if its unique
    return True

def delete_techName():
    return True

def create_tech():
    return True

def delete_tech(): #if tech deleted option to keep Techname or delete all
    return True

def edit_tech():
    return True

def edit_info():
    return True

#______________________________________________________
#Create tech - name(check for duplicate), blocks, details


#______________________________________________________
#Edit tech - details, rearrangement in block, modify/add - blocks, links, 


#______________________________________________________
#Optional - for multiple copy merge tech together
