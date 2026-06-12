from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.find().sort({"rating.grade": -1}).limit(5)

for doc in result:
    print(str(doc.get("title")))