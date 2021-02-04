import pymongo
from pymongo import MongoClient 
from utility.R5config import DB_KEY

R5MemInit = MongoClient(DB_KEY)
db = R5MemInit["R5-test"]
collection = db["test"]

def dbtest():
    queryResult = collection.find({})
    results = []
    for q in queryResult:
        results.append(str(q))
    return results

def dbtest2():
    queryResult = collection.find({}).sort({"_id":-1}).limit(1)
    results = []
    for q in queryResult:
        results.append(str(q))
    return results