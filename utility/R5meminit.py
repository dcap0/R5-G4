import pymongo
from pymongo import MongoClient
from R5config import DB_KEY

R5MemInit = MongoClient(DB_KEY)

db = R5MemInit["R5-test"]
collection = db["test"]

post1={"_id":1,"Mars":"Red"}

collection.insert_one(post1)


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
