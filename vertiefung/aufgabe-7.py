from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.aggregate([
    {
        "$group": {
            "_id": None,
            "avg_time": { "$avg": "$runtime" }
        }
    }
])

for doc in result:
    print("average time: " + str(doc.get("avg_time")))