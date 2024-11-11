from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

vmainDB = client.trialmainDB

vmainCol = vmainDB.tmaincollection
vinfoCol = vmainDB.tinfocollection

# List all databases
print(client.list_database_names())

# Close the connection (optional as it will close automatically when the script ends)
client.close()