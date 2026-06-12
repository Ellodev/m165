from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.find({
    "rating": { "$exists": False }
})
print()
for doc in result:
    print(doc.get("title"))