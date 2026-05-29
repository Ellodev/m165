from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["restaurant"]

def validate_input(input, length):
    if len(input) < length:
        return False
    return True


print("do you want to add a new restaurant? (y/n)")
answer = input()
if answer == "y":
    print("enter the name of the restaurant:")
    name = input()
    if not validate_input(name, 2):
        print("invalid input for name")
        exit()

    print("enter the borough of the restaurant:")
    borough = input()
    if not validate_input(borough, 2):
        print("invalid input for borough")
        exit()

    print("enter the cuisine of the restaurant:")
    cuisine = input()
    if not validate_input(cuisine, 2):
        print("invalid input for cuisine")
        exit()

    print("enter the housenumber of the restaurant (optional):")
    housenumber = input()
    print("enter the street of the restaurant:")
    street = input()
    if not validate_input(street, 2):
        print("invalid input for street")
        exit()
    print("enter the postal code of the restaurant:")
    postalcode = input()
    if not validate_input(postalcode, 5):
        print("invalid input for postal code")
        exit()

    new_restaurant = {
        "name": name,
        "borough": borough,
        "cuisine": cuisine,
        "address": {
            "street": street,
            "building": housenumber,
            "zipcode": postalcode
        },
        "street": street,
        "postalcode": postalcode
    }
    
    db.restaurants.insert_one(new_restaurant)
    print("restaurant added successfully!")