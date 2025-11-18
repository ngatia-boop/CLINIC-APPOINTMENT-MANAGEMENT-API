# backend/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-strong-secret-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    # Try to use DEV_DATABASE_URL first, fallback to default
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL',
        'postgresql://postgres:githehu123@localhost:5432/clinic_db'
    )

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Try to use DATABASE_URL first, fallback to default
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'postgresql://postgres:githehu123@localhost:5432/clinic_db'
    )

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL',
        'postgresql://postgres:githehu123@localhost:5432/clinic_test_db'
    )

# Dictionary to easily access configurations
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
