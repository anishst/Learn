# https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c
# http://zetcode.com/python/pymongo/
# https://www.w3schools.com/python/python_mongodb_getstarted.asp

"""
Shows to how to insert data into a container running in Docker

steps:
Make sure pymongo is install: pip install pymongo
1. launch docker container: docker run -d -p 27017:27017 --name m1 mongo
2. run script below. make sure ip addres matches docker host
3. to verify data insertion lo into container: sudo docker exec -it m1 bash
4. enter mongo in command prompt
5. enter: show dbs to see database

"""
import pymongo  # package for working with MongoDB

client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
# create db
db = client["customersdb"]
# create collection called 'customers'
customers_col = db["customers"]

#  list all mongo dbs
print(client.list_database_names())

# insert one record
mydict = { "name": "John", "address": "Highway 37" }
customers_col.insert_one(mydict)

# insert many records
customers_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Ligy", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
   { "name": "Ligy", "address": "Sideway 1633"}
]
x = customers_col.insert_many(customers_list)
# print list of the _id values of the inserted documents:
print(x.inserted_ids)



# get data and print it
print("show all records in collection; sorted by name")
for x in customers_col.find().sort("name"):
    print(x)
print("show one record in collection")
x = customers_col.find_one()
print(x)

doc_count = customers_col.count_documents(filter={})
print(f"Total count:{doc_count}")

#  filter data by name
filter = {"name":"Ligy"}
sort = [("name",pymongo.ASCENDING)]
skip = 0
limit = 0
doc_count = customers_col.count_documents(filter=filter)
sorted_results = customers_col.find(filter).sort(sort).skip(skip).limit(limit)
# sorted_results = customers.find(filter).sort(sort)
print(f"Filtered count: {doc_count}")

print("sorted")
# get data and print it
for x in sorted_results:
    print(x)

# updating data
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

customers_col.update_one(myquery, newvalues)

print( "Valley 345 updated to Canyon 123 ")
for x in customers_col.find():
  print(x)

# list of all collections in your database
print(db.list_collection_names())

print("Dropping collection....")
customers_col.drop()



