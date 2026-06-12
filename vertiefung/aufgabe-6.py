from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.aggregate([
    {
        "$group": {
            "_id": "$genre",
            "count": { "$sum": 1 }
        }
    }
])

for doc in result:
    print(doc.get("_id") + ": " + str(doc.get("count")))