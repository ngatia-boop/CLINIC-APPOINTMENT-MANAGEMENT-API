# backend/app/api/v1/auth/__init__.py
# This file defines the auth blueprint and imports routes.

from flask import Blueprint  # Import Blueprint for grouping routes

auth_bp = Blueprint('auth', __name__)  # Create auth blueprint

from . import routes  # Import routes to register them with the blueprint
