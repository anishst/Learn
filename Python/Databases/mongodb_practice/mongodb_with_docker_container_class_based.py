# UNDER DEV NOT FULLY WORKING
import uuid

import pymongo


class Database(object):
    URI = "mongodb://192.168.1.50:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['items_test']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):
        Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        return Database.DATABASE[collection].remove(query)



class Items:
    def __init__(self, store, url, desc, target_price, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.store = store
        self.url = url
        self.desc = desc
        self.target_price = target_price

    def __repr__(self):
        return "<Item {} with URL {}>".format(self.store, self.url)

    def save_to_mongo(self):
        Database.update("items_test", {'_id': self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "name": self.store,
            "url": self.url,
            "desc": self.desc,
            "target_price": self.target_price
        }

    def delete(self):
        Database.remove('items_test', {'_id': self._id})

    @staticmethod
    def get_all_items():
        return [elem for elem in Database.find('items_test', {})]

    @staticmethod
    def get_by_id(id):
        return Database.find_one('items_test', {"_id": id})


Database.initialize()
#  add new item
# new_item = Items('amazon', 'url', 'desc1', '30')
# new_item.save_to_mongo()
# print(len(new_item.get_all_items()))



all_items = Database.find('items_test',{})
for item in all_items:
    print(item["_id"])
    print(item["name"])
    print(item["url"])

# get by id
print(Items.get_by_id('67913520e1af4ca2b0ed7f9abb5b5019'))

# delete item
Items.delete()
# total count
print(len(Items.get_all_items()))


