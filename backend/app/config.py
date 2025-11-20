# backend/app/config.py
# This file defines configuration classes for different environments (development, production, testing).
# It uses environment variables for sensitive data like database URLs and secrets.

import os  # Import os to access environment variables

class Config:
    """
    Base configuration class with common settings.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'  # Secret key for sessions and JWT; use env var in production
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///clinic.db'  # Database URI; defaults to SQLite for dev
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable SQLAlchemy event system for performance
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'  # Secret key for JWT tokens
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS') or '*'  # Allowed origins for CORS; restrict in production

class DevelopmentConfig(Config):
    """
    Configuration for development environment.
    Enables debug mode and detailed error pages.
    """
    DEBUG = True  # Enable debug mode for detailed error messages
    SQLALCHEMY_ECHO = True  # Log all SQL queries for debugging

class ProductionConfig(Config):
    """
    Configuration for production environment.
    Disables debug mode and enforces security settings.
    """
    DEBUG = False  # Disable debug mode
    # Ensure SECRET_KEY and JWT_SECRET_KEY are set via environment variables
    # Use a production database like PostgreSQL

class TestingConfig(Config):
    """
    Configuration for testing environment.
    Uses an in-memory database for fast tests.
    """
    TESTING = True  # Enable testing mode
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests
    WTF_CSRF_ENABLED = False  # Disable CSRF for easier testing
