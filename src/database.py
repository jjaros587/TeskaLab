import pymongo
from src.singleton import singleton


@singleton
class Database:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.collection = self.client['db']['containers']

    def save_data(self, data):
        self.collection.insert_many(data)

    def get_data(self):
        return self.collection.find()

    def delete_data(self):
        self.collection.remove()
