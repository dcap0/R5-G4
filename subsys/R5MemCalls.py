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
        results.append(str(q["name"]))
    return results

def getCurrentPlanet():
    queryResult = planets.find({})
    results = []
    for q in queryResult:
        results.append(str(q["name"])+ ":\n" + str(q["description"]) + "\n")
    return results[len(results) - 1]

