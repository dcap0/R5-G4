# from pymongo import MongoClient

# R5MemInit = MongoClient('localhost', 27017)

# db = R5MemInit.test_database
#
# # print(db.list_collection_names()) shows all collection names
#
# testCollection = db["test"]
#
# # testCollection.insert_one({"test2":"data2"}) Inserts a particular data piece.
# # print(testCollection.find_one({"test":"data"})) Prints the specific key:pair and its ID
#
# #prints out each key:pair
# for test in testCollection.find():
#     print(test)
#
# query = {"test2":"data2"}
# replace = {"testAlpha":"dataAlpha"}
#
# testCollection.update_one(query,replace)
#
# for test in testCollection.find():
#     print(test)
#
#



