# backend/app/__init__.py
# This file contains the application factory function to create and configure the Flask app.
# It follows the factory pattern to allow for different configurations (e.g., development, production).

from flask import Flask  # Import Flask to create the app instance
from .config import Config  # Import the configuration class
from .extensions import db, migrate, jwt, cors, ma  # Import initialized extensions
from .api.v1.auth import auth_bp  # Import the auth blueprint
from .api.v1.appointments import appointments_bp  # Import the appointments blueprint
from .api.v1.users import users_bp  # Import the users blueprint

def create_app(config_class=Config):
    """
    Application factory function.
    Creates and configures the Flask application with all necessary components.

    Args:
        config_class: The configuration class to use (default: Config)

    Returns:
        Flask app instance
    """
    app = Flask(__name__)  # Create a new Flask app instance
    app.config.from_object(config_class)  # Load configuration from the config class

    # Initialize extensions with the app
    db.init_app(app)  # Initialize SQLAlchemy database
    migrate.init_app(app, db)  # Initialize Flask-Migrate for database migrations
    jwt.init_app(app)  # Initialize Flask-JWT-Extended for authentication
    cors.init_app(app)  # Initialize Flask-CORS for cross-origin requests
    ma.init_app(app)  # Initialize Flask-Marshmallow for serialization

    # Register blueprints for API routes
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')  # Register auth blueprint with prefix
    app.register_blueprint(appointments_bp, url_prefix='/api/v1/appointments')  # Register appointments blueprint
    app.register_blueprint(users_bp, url_prefix='/api/v1/users')  # Register users blueprint

    # Register custom CLI commands
    from .cli import register_commands
    register_commands(app)

    # Additional app setup can be added here (e.g., error handlers)

    return app  # Return the configured app instance
