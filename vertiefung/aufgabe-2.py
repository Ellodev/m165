from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.find({"runtime": {"$gt": 150}})
for doc in result:
    print(doc.get("title"))