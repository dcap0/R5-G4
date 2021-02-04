import pymongo
from pymongo import MongoClient
from R5config import DB_KEY

R5MemInit = MongoClient(DB_KEY)

db = R5MemInit["R5-mem"]
collection = db["planetData"]

# post1={"_id":1,"Mars":"Red"}

# collection.insert_one(post1)

pname1 = "The Wheel"
pdes1 = "Formerly known as space station BDT-0978. Located in the Besh Gorgon system in the Mid Rim. Divided into levels hosting casinos, cantinas, sports arenas, and a variety of shops. Currently known to be hosting a large underworld presence..."


def insertPlanet(name:str,description:str):
    pid = collection.count_documents({})
    post = {
        "name": name,
        "description": description,
        "planetId": pid
    }
    collection.insert_one(post)



print("Inserting Planet")
insertPlanet(pname1,pdes1)

# search via dictionary
# results = collection.find({"hello":"world"})

# print results
# for result in results:
#     print(result)

# print the value of key _id
# for r in results:
#    print(r["_id"])

# # query by _id
# resultz = collection.find({"_id":0})

# for r in resultz:
#     print(r)

# update an existing record
# collection.update_one({"_id":0},{"$set":{"hello":"goodbye"}})
