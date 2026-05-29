from pymongo import MongoClient
import os

mongoConnectionString = os.environ["MONGO_URI"]

client = MongoClient(mongoConnectionString)
db = client["restaurant"]

#habe nicht wirklich getestet mit cloud da es freiwillig ist, aber sollte gehen