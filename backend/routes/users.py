from flask import Blueprint, jsonify, request
import uuid
from ..storage.memory import users

bp = Blueprint('users', __name__, url_prefix='/api')

@bp.route('/users', methods=['GET'])
def list_users():
    return jsonify(users)

@bp.route('/user', methods=['POST'])
def create_user():
    # Parse JSON body
    data = request.get_json() or {}

    # Use defaults if keys are missing
    first_name = data.get("first_name", "Bruce")
    last_name = data.get("last_name", "Wayne")

    # Generate unique user ID
    user_id = str(uuid.uuid4())

    # Store user in memory
    users[user_id] = {
        "user_id": user_id,
        "first_name": first_name,
        "last_name": last_name
    }

    # Return the new user's ID
    return jsonify({"user_id": user_id}), 201
