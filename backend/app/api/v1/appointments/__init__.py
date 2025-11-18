# backend/app/api/v1/appointments/__init__.py
# This file defines the appointments blueprint and imports routes.

from flask import Blueprint  # Import Blueprint for grouping routes

appointments_bp = Blueprint('appointments', __name__)  # Create appointments blueprint

from . import routes  # Import routes to register them with the blueprint
