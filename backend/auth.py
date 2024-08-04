from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from config import Config

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()
jwt = JWTManager()

users = {}

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    users[username] = hashed_password
    return jsonify({'message': 'User registered successfully'}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username not in users or not bcrypt.check_password_hash(users[username], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    access_token = create_access_token(identity=username)
    return jsonify({'access_token': access_token}), 200


