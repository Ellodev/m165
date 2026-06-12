from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.count_documents({"director": "Christopher Nolan"})
print("there are " + str(result) + " made by christopher nolan")