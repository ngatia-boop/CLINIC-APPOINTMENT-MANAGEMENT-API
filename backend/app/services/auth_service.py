# backend/app/services/auth_service.py
# This file contains business logic for authentication services.

from ..models import User  # Import User model
from ..extensions import db  # Import database instance
from flask_jwt_extended import create_access_token  # For JWT token creation
from werkzeug.exceptions import BadRequest  # For error handling

class AuthService:
    """
    Service class for authentication-related operations.
    """

    @staticmethod
    def register_user(data):
        """
        Register a new user.

        Args:
            data: Dictionary with user data (username, email, password, etc.)

        Returns:
            User object if successful

        Raises:
            BadRequest: If user already exists
        """
        # Check if user already exists
        if User.query.filter_by(email=data['email']).first():
            raise BadRequest('User with this email already exists')
        if User.query.filter_by(username=data['username']).first():
            raise BadRequest('Username already taken')

        # Create new user
        user = User(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data.get('role', 'patient')
        )
        user.set_password(data['password'])

        # Save to database
        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def authenticate_user(username, password):
        """
        Authenticate a user with username and password.

        Args:
            username: User's username
            password: User's password

        Returns:
            Access token if successful

        Raises:
            BadRequest: If credentials are invalid
        """
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            raise BadRequest('Invalid credentials')

        # Create JWT token
        access_token = create_access_token(identity=str(user.id))
        return access_token
