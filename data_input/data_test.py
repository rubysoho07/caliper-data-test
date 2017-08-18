from pymongo import MongoClient
import pprint
import re

client = MongoClient('mongodb://localhost:27017')
db = client['test']
event_collection = db['mongoEvent']

pprint.pprint(event_collection.find_one())

pattern = re.compile(".*Submitted$")
print("Action(Submitted) : " + str(event_collection.find({"event.action": pattern}).count()))
