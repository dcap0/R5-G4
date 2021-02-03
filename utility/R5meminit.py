import pymongo
from pymongo import MongoClient

R5MemInit = MongoClient("mongodb+srv://R5:EAiGu4TH4I2SMmy2@r5-mem.7lkv7.mongodb.net/R5-mem?retryWrites=true&w=majority")

db = R5MemInit["R5-test"]
collection = db["test"]

post = {"_id":0,"name":"ddmac"}
post1={"_id":1,"name":"daniel"}

collection.insert_many([post,post1])


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
