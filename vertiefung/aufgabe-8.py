from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.find({
    "$and": [
        {"genre": "Drama"},
        {"rating.grade": {"$gt": 8.5}},
        {"runtime": {"$lt": 180}}
    ]
})

for doc in result:
    print(str(doc.get("title")))