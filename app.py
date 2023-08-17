from flask import Flask,  request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client["test"]
collections = db["test"]


@app.route('/')
def index():
    users = list(collections.find({}, {'_id':0}))
    
    if users:
        return jsonify(users)
    else:
        return jsonify({"error": "User not found"}), 404
    
    

if __name__ == '__main__':
    app.run(debud=True)