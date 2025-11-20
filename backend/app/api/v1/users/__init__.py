# backend/app/api/v1/users/__init__.py
# This file defines the users blueprint and imports routes.

from flask import Blueprint  # Import Blueprint for grouping routes

users_bp = Blueprint('users', __name__)  # Create users blueprint

from . import routes  # Import routes to register them with the blueprint
