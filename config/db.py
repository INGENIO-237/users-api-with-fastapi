from pymongo import MongoClient

# Connect to the local instance of mongodb server
db = MongoClient()

# You can also use a specific mongoDB server by passing its
# address in the parenthesis of MongoClient() above