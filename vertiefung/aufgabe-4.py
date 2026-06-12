from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["media"]
collection = db["movies"]

result = collection.count_documents({
    "comments.text": { "$regex": "spannend", "$options": "i" }
})
print("there are " + str(result) + " comments with spannend")