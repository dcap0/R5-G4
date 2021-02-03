import pymongo
from pymongo import MongoClient

R5MemInit = MongoClient("mongodb+srv://R5:AMP4ebTru8cCgqh1@r5-mem.7lkv7.mongodb.net/R5test?retryWrites=true&w=majority")

db = R5MemInit["R5test"]
collection = db["testing"]

# post = {"_id":1,"it's":"working!"}

# collection.insert_one(post)


# search via dictionary
results = collection.find({"hello":"world"})

# print results
# for result in results:
#     print(result)

#print the value of key _id
#for r in results:
#    print(r["_id"])

#query by _id
# resultz = collection.find({"_id":0})

# for r in resultz:
#     print(r)


collection.update_one({"_id":0},{"$set":{"hello":"goodbye"}})