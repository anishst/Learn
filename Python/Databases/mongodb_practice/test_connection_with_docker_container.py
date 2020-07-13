# https://medium.com/codervlogger/python-mongodb-tutorial-using-docker-52f330852b4c
# http://zetcode.com/python/pymongo/

"""
Shows to how to insert data into a container running in Docker

steps:
1. launch docker container: docker run -d -p 27017:27017 --name m1 mongo
2. run script below. make sure ip addres matches docker host
3. to verify data insertion lo into container: sudo docker exec -it m1 bash
4. enter mongo in command prompt
5. enter: show dbs to see database

"""
import pymongo  # package for working with MongoDB
client = pymongo.MongoClient("mongodb://192.168.1.35:27017/")
db = client["customersdb"]
customers = db["customers"]
customers_list = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
   { "name": "lig", "address": "Sideway 1633"}
]
x = customers.insert_many(customers_list)
# print list of the _id values of the inserted documents:
print(x.inserted_ids)

# get data and print it
for x in customers.find():
    print(x)

n_record = db.customers.find().count()
print(n_record)




