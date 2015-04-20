from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.modoc
dbOffender = db.db_offenders
print [x for x in dbOffender.find()]
