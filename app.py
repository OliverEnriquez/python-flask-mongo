from flask import Flask,  request, jsonify
from DbConnection import DbConnection

app = Flask(__name__)
collections = DbConnection.connect()

""" get users """
@app.route('/')
def index():
    users = list(collections.find({}, {'_id':0}))
    
    if users:
        return jsonify(users)
    else:
        return jsonify({"error": "User not found"}), 404
    

"""Find user"""
@app.route("/user/<name>", methods= ['GET'])
def findUser(name):
    user = collections.find_one({'name': name}, {'_id': 0})
        
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

""" Add users """
@app.route('/user', methods= ['POST'])
def addUser():
    data = request.get_json()
    collections.insert_one(data)
    return jsonify({"message": " Added user"}), 201

"""Remove user"""
@app.route('/user/delete/<name>', methods=['DELETE'])
def deleteUser(name):
    result = collections.delete_one({'name': name})
    
    if result.deleted_count > 0 :
        return jsonify({'message': 'Data deleted successfully'}), 200
    else:
        return jsonify({'message': 'Data not found'}), 404



if __name__ == '__main__':
    app.run(debud=True)