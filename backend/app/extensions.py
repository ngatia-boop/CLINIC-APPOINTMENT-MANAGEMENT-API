# backend/app/extensions.py
# This file initializes all Flask extensions to avoid circular imports.
# Extensions are created here and initialized in the app factory.

from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy for database ORM
from flask_migrate import Migrate  # Flask-Migrate for database migrations
from flask_jwt_extended import JWTManager  # JWTManager for JSON Web Tokens
from flask_cors import CORS  # CORS for cross-origin resource sharing
from flask_marshmallow import Marshmallow  # Marshmallow for serialization and validation

# Create extension instances without initializing them yet
db = SQLAlchemy()  # Database instance
migrate = Migrate()  # Migration instance
jwt = JWTManager()  # JWT manager instance
cors = CORS()  # CORS instance
ma = Marshmallow()  # Marshmallow instance
