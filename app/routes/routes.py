from flask import Blueprint, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return jsonify(message="API is running")

@routes.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"])

@routes.route('/login', methods=['GET'])
def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token)

@routes.route('/protected', methods=['POST'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")
