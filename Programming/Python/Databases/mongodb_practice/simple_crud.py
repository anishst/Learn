# https://medium.com/swlh/basic-c-r-u-d-with-pymongo-3a33a04dec8f
# https://www.w3schools.com/python/python_mongodb_getstarted.asp

import pymongo
client = pymongo.MongoClient("192.168.1.50:27017")
db = client['database_name']
printer_collection = db['printer_collection']

print("Adding new items...")
printer_a = {'printer_name': 'X Printer Co', 'printer_model': 231901, 'price': 250.00}
printer_b = {'printer_name': 'X Printer Co', 'printer_model': 938901, 'price': 450.00}
printer_c = {'printer_name': 'Hyper Global Printers Inc', 'printer_model': 901, 'price': 299.00}
# printer_d_custom_id = {"_id" : '23333' ,'printer_name': 'anish printer', 'printer_model': 901, 'price': 299.00}

# results = printer_collection.insert_many([printer_a, printer_b, printer_c, printer_d_custom_id])
results = printer_collection.insert_many([printer_a, printer_b, printer_c])

print("Listing all items....")
query = printer_collection.find({})
for item in query:
    print(item)

print("\nListing one item....")
x = printer_collection.find_one()
print(x["_id"])

print("\nListing all printers....")
query = printer_collection.find({}, {'printer_name':1})
for item in query:
    print(item["printer_name"])


print("\nSorting by name")
mydoc = printer_collection.find().sort("printer_name")
for x in mydoc:
  print(x)

print("\nSorting by name DESC")
mydoc = printer_collection.find().sort("printer_name",-1)
for x in mydoc:
  print(x)

print("\n Return only some filed")
for x in printer_collection.find({},{ "_id": 0, "printer_name": 1}):
  print(x)

print("\n Query using printer  name and model number")
myquery = { "printer_name": "X Printer Co" , "printer_model": 231901}
mydoc = printer_collection.find(myquery)
for x in mydoc:
  print(x)

# print("\n Find one using id")
# mydoc = printer_collection.find_one({'_id': '23333'})
# for x in mydoc:
#   print(x)


print("\n Original prices")
query = printer_collection.find({}, {'price':1})
for item in query:
    print(item)

print("\n Making Price Change")
printer_c_name = {'printer_name': 'Hyper Global Printers Inc'}
printer_c_price_update = {'$set': {'price': 199.00}}
printer_collection.update_one(printer_c_name, printer_c_price_update)
#New Price:
query = printer_collection.find({}, {'price':1})
for item in query:
    print(item)

print("\n Deleting Hyper Global Printers Inc\n")
delete_printer = printer_collection.delete_one({'printer_name': 'Hyper Global Printers Inc'})
query = printer_collection.find({}, {'printer_name':1})
for item in query:
    print(item)

# drop collection
# printer_collection.drop()
# print("\nDropped collection!")