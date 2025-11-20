# backend/app/api/v1/auth/routes.py
# This file defines authentication routes (register, login).

from flask import request  # For request handling
from flask_jwt_extended import jwt_required  # For JWT protection
from app.schemas import user_schema  # Import user schema
from app.services import AuthService  # Import auth service
from app.utils import create_response  # Import response helper
from . import auth_bp  # Import auth blueprint

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    Expects JSON with username, email, password, confirm_password, first_name, last_name, role.
    """
    data = request.get_json()  # Get JSON data from request
    errors = user_schema.validate(data)  # Validate input data
    if errors:
        return create_response(message='Validation errors', status=400)

    try:
        user = AuthService.register_user(data)  # Register user via service
        result = user_schema.dump(user)  # Serialize user
        return create_response(data=result, message='User registered successfully', status=201)
    except Exception as e:
        return create_response(message=str(e), status=400)

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login a user.
    Expects JSON with username and password.
    Returns JWT token.
    """
    data = request.get_json()  # Get JSON data
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return create_response(message='Username and password required', status=400)

    try:
        token = AuthService.authenticate_user(username, password)  # Authenticate user
        return create_response(data={'access_token': token}, message='Login successful')
    except Exception as e:
        return create_response(message=str(e), status=401)

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()  # Require JWT token
def profile():
    """
    Get current user profile.
    Requires authentication.
    """
    from app.utils import get_current_user
    user = get_current_user()  # Get user from token
    if not user:
        return create_response(message='User not found', status=404)

    result = user_schema.dump(user)  # Serialize user
    return create_response(data=result)
