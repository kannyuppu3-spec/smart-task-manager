from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app.models.user_model import User

auth = Blueprint('auth', __name__)
@auth.route('/register', methods=['POST'])

def register():

    data = request.get_json()

    username = data.get('username')

    email = data.get('email')

    password = data.get('password')

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:

        return jsonify({
            "message": "User already exists"
        }), 400

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)

    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201
@auth.route('/login', methods=['POST'])

def login():

    data = request.get_json()

    email = data.get('email')

    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:

        return jsonify({
            "message": "User not found"
        }), 404

    if check_password_hash(user.password, password):

        return jsonify({
            "message": "Login successful"
        }), 200

    return jsonify({
        "message": "Invalid password"
    }), 401