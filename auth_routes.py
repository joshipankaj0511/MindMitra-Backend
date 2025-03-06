from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from functools import wraps
from config import users  # MongoDB 'users' collection import
from flask import current_app as app

auth_routes = Blueprint('auth_routes', __name__)

# 🔹 Middleware for Protected Routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return jsonify({"error": "Token is missing!"}), 401

        try:
            token = token.split(" ")[1]  # Bearer <token>
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated

# 🔹 Protected Route
@auth_routes.route('/protected-route', methods=['GET'])
@token_required
def protected():
    return jsonify({"message": "This is a protected route, access granted!"}), 200

# 🔹 User Signup API
@auth_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not (username and email and password):
        return jsonify({"error": "All fields are required"}), 400

    if users.find_one({"email": email}):
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(password)
    users.insert_one({"username": username, "email": email, "password": hashed_password})

    return jsonify({"message": "User registered successfully"}), 201

# 🔹 User Login API
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = users.find_one({"email": email})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT Token
    token = jwt.encode({
        "email": email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token, "message": "Login successful"}), 200
