import os
from pymongo import MongoClient

# setup the mongo db connection
mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
client = MongoClient(mongo_uri)
db = client['test_db']

# create a new collection for the todos
todos_collection = db['todos']

