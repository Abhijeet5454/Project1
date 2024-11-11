#Setup connection with MongoDB database
from pymongo import MongoClient

# Connection URL
client = MongoClient("mongodb://localhost:27017/")

# Access a specific database
db = client["mydatabase"]

print("Connected to MongoDB!")

# Create a new database and collection
db = client["mydatabase"]
collection = db["mycollection"]


# Insert a single document
document = {"name": "Alice", "age": 25}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)

# Insert multiple documents
documents = [
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
result = collection.insert_many(documents)
print("Inserted document IDs:", result.inserted_ids)


# Find one document
person = collection.find_one({"name": "Alice"})
print("Found document:", person)

# Find all documents
people = collection.find()
for person in people:
    print(person)


# Update a single document
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})

# Update multiple documents
collection.update_many({"age": {"$gt": 30}}, {"$set": {"status": "Senior"}})


# Delete a single document
collection.delete_one({"name": "Bob"})

# Delete multiple documents
collection.delete_many({"age": {"$lt": 30}})



# Create an index on the "name" field
collection.create_index("name")


# Perform aggregation (e.g., calculate average age)
pipeline = [
    {"$group": {"_id": None, "average_age": {"$avg": "$age"}}}
]
result = collection.aggregate(pipeline)
for doc in result:
    print("Average age:", doc["average_age"])


# Start a session for transactions
with client.start_session() as session:
    with session.start_transaction():
        collection.insert_one({"name": "Transaction Test", "age": 40}, session=session)
        collection.delete_one({"name": "Charlie"}, session=session)


try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]

    # Perform some operations
    collection.insert_one({"name": "Dave", "age": 28})

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    client.close()
