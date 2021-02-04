import pymongo
from pymongo import MongoClient 
from utility.R5config import DB_KEY

R5MemInit = MongoClient(DB_KEY)
db = R5MemInit["R5-mem"]
planets = db["planetData"]
players = db["playerData"]

def getPlanetList():
    queryResult = planets.find({})
    results = []
    for q in queryResult:
        results.append(str(q))
    return results