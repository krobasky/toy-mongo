import sys
from pymongo import MongoClient
import pprint

##
print("+ ** Open connection")
mongo_client = MongoClient('mongodb://localhost:27020')
db_list = mongo_client.list_database_names()

##
print("+ ** Connect to db demo")
if "toys" in db_list:
    print("+ WARN: The toys database exists, using that.")
else:
    print("+ The toys database dosn't exist, create it.")
    res = mongo_client.drop_database("toys")
    pprint.pprint(res)

db = mongo_client.toys

print("+ ** Set up collection ")
print("+ existing collections:%s" % db.list_collection_names())
if "vintage_dolls" in db.list_collection_names():
    print("+ vintage_dolls collection exists, drop it, result:")
    res =db.vintage_dolls.drop()
    pprint.pprint(res)
    print("+ now: :%s" % db.list_collection_names())
print("+ creating new vintage_dolls collection")
dolls = db.vintage_dolls
print("+ now: :%s" % db.list_collection_names())
print("+ inserting dolls, res = ")
res = dolls.insert_many([ {"name": "Dawn", "type": "fashion", "year": 1970},
                          {"name": "Raggedy Ann", "type": "play", "year": 1880},
                          {"name": "The Lawyers", "type": "Kewpie", "year": 1912} ])
pprint.pprint("acknowledged=%s"%res.acknowledged)
pprint.pprint(res.inserted_ids)

print("+ print dolls:")
for doll in dolls.find():
    pprint.pprint(doll)


print("+ setup done.")

##
print("+ ** Get collection demo")

print("+ try to drop non-existent foo collection.")
res =db.drop_collection("foo")
pprint.pprint(res)

print("+ number of vintage dolls found:")
print(dolls.count_documents({}))

print("+ print dolls:")
dolls_docs = dolls.find()
for doc in dolls_docs:
    pprint.pprint(doc)

# dolls_docs is a cursor and must be reset for each loop

##
print("+ ** Insert document demo")

print("+ insert doll:")
doll = {"name": "Purple Bunnybee", "type": "cabbage patch kids", "year": 1982}
pprint.pprint(doll)
doll_id = dolls.insert_one( doll ).inserted_id
print("+ new doll id = ")
pprint.pprint(doll_id)


print("+ insert doll:")
doll = {"name": "Raggedy Andy", "type": "play", "year": 1918}
pprint.pprint(doll)
doll_id = dolls.insert_one( doll ).inserted_id
print("+ new doll id = ")
pprint.pprint(doll_id)

print("+ print dolls, plus 2  new ones")
dolls_docs = dolls.find()
for doc in dolls_docs:
    print(doc)

##
print("+ ** Find document demo")
print("+ Find a doll:")
pprint.pprint(dolls.find_one())
print("+ Find a play doll:")
pprint.pprint(dolls.find_one({"type": "play"}))
print("+ Find all play dolls:")
for doll in dolls.find({"type": "play"}):
    pprint.pprint(doll)
print("+ Find a non-existent doll (foo):")
pprint.pprint(dolls.find_one({"type": "foo"}))

##
print("+ ** Delete demo")

print("+ delete first doc:")
result = dolls.find_one_and_delete({})
print("+ document deleted:")
print(result)
print(result.values())
print(result["_id"])
print(result['name'])

print("+ print dolls minus first one")
dolls_docs = dolls.find()
for doc in dolls_docs:
    print(doc)

print("+ delete The Lawyers by name, result:")
res=dolls.find_one_and_delete({"name":"The Lawyers"})
pprint.pprint(res)
print("+ print docs minus The Lawyers")
for doc in dolls.find({}):
    print(doc)

##
print("+ ** Update demo")
print("+ update Bunnybee's year")
dolls.find_one_and_update({"name":"Purple Bunnybee"}, {'$set':{'year':2020}})
print("+ print docs with new year")
for doc in dolls.find({}):
    print(doc)



## delete nothing (xxx???)
#result3=dolls.delete_many({'_id': '61df3b7a21d91f1f0f1cb211'}) # don't use string representation
#print(result3.deleted_count)
## still has 2 docs (xxx??)
#for doc in dolls.find({}):
#    print(doc)

