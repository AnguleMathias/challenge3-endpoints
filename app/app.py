
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'mathias',
        'email': 'angule@gmail.com',
        'password': '123456',
    },
    {
        'id': 2,
        'name': 'Mimi',
        'email': 'wewe@gmail.com',
        'password': 'sisisi',
    }
]


# home route
@app.route('/')
def index():
    return "Welcome user!"


# get all users
@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


# get a single user by ID
@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


# add user
@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json.get('description', "", "")
    }
    users.append(user)
    return jsonify({'user': user}), 201


# update user
@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']):
        abort(400)
    if 'password' in request.json and type(request.json['password']):
        abort(400)
    if 'email' in request.json and type(request.json['email']):
        abort(400)

    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['email'] = request.json.get('email', user[0]['email'])

    return jsonify({'user': user[0]})


# delete user
@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})


# handle error
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Item not found'}), 404)
