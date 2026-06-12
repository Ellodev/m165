from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.aggregate([
    {
        "$group": {
            "_id": "$genre",
            "avg_rating": { "$avg": "$rating.grade" }
        }
    }
])

for doc in result:
    print("average rating for " + doc.get("_id") + ": " + str(doc.get("avg_rating")))