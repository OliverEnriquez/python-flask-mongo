from pymongo import MongoClient

class DbConnection:
    def connect():
        client = MongoClient('localhost', 27017)
        db = client["test"]
        return db["users"]