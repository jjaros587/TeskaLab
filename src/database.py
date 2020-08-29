import pymongo
from src.utils import singleton
from jaraco.docker import is_docker


@singleton
class Database:

    host = "mongo" if is_docker() else "localhost"

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://%s:27017/" % self.host)
        self.collection = self.client['db']['containers']

    def save_data(self, data):
        self.collection.insert_many(data)

    def get_data(self):
        return self.collection.find()

    def delete_data(self):
        self.collection.remove()
