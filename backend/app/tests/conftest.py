# backend/app/tests/conftest.py
# This file contains pytest fixtures for testing.

import pytest  # For testing framework
from .. import create_app  # Import app factory
from ..config import TestingConfig  # Import test config
from ..extensions import db  # Import database

@pytest.fixture
def app():
    """
    Create and configure a test app instance.
    """
    app = create_app(TestingConfig)  # Create app with test config
    with app.app_context():
        db.create_all()  # Create all tables
        yield app
        db.session.remove()  # Clean up session
        db.drop_all()  # Drop all tables

@pytest.fixture
def client(app):
    """
    A test client for the app.
    """
    return app.test_client()
