import pymongo
from pymongo import MongoClient

R5MemInit = MongoClient("mongodb+srv://R5:AMP4ebTru8cCgqh1@r5-mem.7lkv7.mongodb.net/R5test?retryWrites=true&w=majority")

db = R5MemInit["R5test"]
collection = db["testing"]

post = {"_id":1,"it's":"working!"}

collection.insert_one(post)




