# backend/app/utils/helpers.py
# This file contains helper functions used across the application.

from flask import jsonify  # For JSON responses
from ..extensions import jwt  # For JWT operations

def create_response(data=None, message=None, status=200):
    """
    Create a standardized JSON response.

    Args:
        data: Data to include in response
        message: Message string
        status: HTTP status code

    Returns:
        JSON response
    """
    response = {}
    if message:
        response['message'] = message
    if data is not None:
        response['data'] = data
    return jsonify(response), status

def get_current_user():
    """
    Get the current user from JWT token.

    Returns:
        User object or None
    """
    from flask_jwt_extended import get_jwt_identity
    from ..models import User

    user_id = get_jwt_identity()
    if user_id:
        return db.session.get(User, int(user_id))
    return None

def require_role(required_role):
    """
    Decorator to require a specific role for a route.

    Args:
        required_role: Role required (e.g., 'admin', 'doctor')

    Returns:
        Decorator function
    """
    def decorator(f):
        from functools import wraps
        from flask import abort

        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = get_current_user()
            if not user or user.role != required_role:
                abort(403)  # Forbidden
            return f(*args, **kwargs)
        return decorated_function
    return decorator
