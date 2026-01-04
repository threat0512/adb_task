import os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
client = MongoClient(mongo_uri)
db = client['test_db']

todos_collection = db['todos']

