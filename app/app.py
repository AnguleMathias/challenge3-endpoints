import re
import os
from flask import Flask, jsonify, abort, request, make_response
from flask_jwt_extended import jwt_required, JWTManager
from flask_bcrypt import Bcrypt
from .models import Database
from flask_cors import CORS, cross_origin


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
jwt = JWTManager(app)
CORS(app)
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    if request.method == 'GET':
        welcome_message = {"Message": [{
            "Welcome": "Welcome to my Diary API"
        }]}

        response = {"status": "success", "Message": welcome_message}
        return response, 200


@app.route('/api/v1/entries', methods=['GET', 'POST'])
@jwt_required
@cross_origin()
def entries():

    if request.method == 'GET':
        Database().create_table_entry()
        return Database().get_all_entries()

    else:
        if not request.json:
            abort(400)
        elif 'title' not in request.json:
            return jsonify({'message': 'Title is required'}), 400
        elif 'entry' not in request.json:
            return jsonify({'message': 'Entry is required'}), 400
        elif 'user_id' not in request.json:
            return jsonify({'message': 'Sign in is required'}), 400

        user_id = request.json['user_id']
        title = request.json['title']
        entry = request.json['entry']

        entry_data = {
            'user_id': user_id,
            'title': title,
            'entry': entry
        }

        Database().create_table_entry()
        return Database().add_entry(entry_data)


@app.route('/api/v1/entries/<int:entry_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
@cross_origin()
def modify_entries(entry_id):
    if request.method == 'GET':
        Database().create_table_entry()
        return Database().get_one_entry(entry_id)
    elif request.method == 'PUT':
        title = request.json['title']
        entry = request.json['entry']
        entry_data = {
            'title': title,
            'entry': entry
        }
        Database().create_table_entry()
        return Database().update_entry(entry_id, entry_data)

    else:
        Database().create_table_entry()
        return Database().delete_entry(entry_id)


@app.route('/auth/signup', methods=['POST'])
@cross_origin()
def signup():
    if not request.json:
        return ({'message': 'Request should be in json format'}), 400
    elif not 'username' in request.json:
        return jsonify({'message': 'Username is required'}), 400
    elif not 'email' in request.json:
        return jsonify({'message': 'Email is required'}), 400
    elif not 'password' in request.json:
        return jsonify({'message': 'Password is required'}), 401
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    hashed_password = bcrypt.generate_password_hash(password).decode('UTF-8')

    valid_email = re.compile(r"(^[a-zA-Z0-9_.-]+@[a-zA-Z-]+\.[.a-zA-Z-]+$)")
    valid_username = re.compile(r"(^[a-zA-Z0-9_.-]+$)")
    if not re.match(valid_username, username):
        return jsonify({'message': 'Username should not have any special characters.'}), 400
    elif len(username) < 3:
        return jsonify({'message': 'Username should be at least three characters long.'}), 400
    elif len(password) < 8:
        return jsonify({'message': 'Password should be at least eight characters long.'}), 400
    elif not re.match(valid_email, email):
        return jsonify({'message': 'Invalid email format.'}), 400
    user_data = {
        'username': username,
        'password': hashed_password,
        'email': email
    }
    Database().create_table_user()
    return Database().signup(user_data)


@app.route('/auth/login', methods=['POST'])
@cross_origin()
def login():
    if not request.json:
        abort(400)
    elif 'username' not in request.json:
        return jsonify({'message': 'Username is required'}), 400
    elif 'password' not in request.json:
        return jsonify({'message': 'Password is required'}), 401

    username = request.json['username']
    password = request.json['password']

    Database().create_table_user()

    return Database().login(username, password)
