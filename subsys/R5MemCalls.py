import pymongo
from pymongo import MongoClient 

R5MemInit = MongoClient("")
db = R5MemInit["R5-test"]
collection = db["test"]


def dbtest():
    queryResult = collection.find({})
    results = []
    for q in queryResult:
        results.append(str(q))
    return results