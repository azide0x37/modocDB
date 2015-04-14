from pymongo import MongoClient

client = MongoClient()
db = client.modoc
dbOffender = db['db_offender']
print dbOffender.find_one()
