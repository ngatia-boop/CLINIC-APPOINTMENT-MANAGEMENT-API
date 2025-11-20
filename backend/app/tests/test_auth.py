# backend/app/tests/test_auth.py
# This file contains tests for authentication functionality.

import pytest  # For testing framework
from ..models import User  # Import User model
from ..services import AuthService  # Import AuthService
from ..extensions import db  # Import database

def test_register_user(app):
    """
    Test user registration.
    """
    with app.app_context():
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        user = AuthService.register_user(data)
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'

def test_register_duplicate_user(app):
    """
    Test registering a user with existing username or email.
    """
    with app.app_context():
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        AuthService.register_user(data)
        with pytest.raises(Exception):
            AuthService.register_user(data)

def test_authenticate_user(app):
    """
    Test user authentication.
    """
    with app.app_context():
        # Create user
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'password123',
            'confirm_password': 'password123',
            'first_name': 'Test',
            'last_name': 'User'
        }
        AuthService.register_user(data)

        # Authenticate
        token = AuthService.authenticate_user('testuser', 'password123')
        assert token is not None

def test_authenticate_invalid_user(app):
    """
    Test authentication with invalid credentials.
    """
    with app.app_context():
        with pytest.raises(Exception):
            AuthService.authenticate_user('invalid', 'password')
