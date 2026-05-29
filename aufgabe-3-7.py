from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant"]

def validate_input(input, length):
    if len(input) < length:
        return False
    return True


print("do you want to delete a restaurant? (y/n)")
answer = input()
if answer == "y":
    print("enter the name of the restaurant:")
    name = input()
    if not validate_input(name, 2):
        print("invalid input for name")
        exit()

    count =db.restaurants.count_documents({"name": name})

    print("there are " + str(count) + " restaurants with the name " + name)
    answer = input("do you want to delete all of them? (y/n)")
    if answer == "y":
        db.restaurants.delete_many({"name": name})
        print("restaurants deleted successfully!")
    else:
        print("deletion cancelled!")