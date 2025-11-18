# backend/app.py

import os
from flask import Flask
from .config import config
from .extensions import db, migrate, api, cors

# Import models to ensure they are registered with SQLAlchemy
from .models import Patient, Doctor, Appointment, Service, DoctorService 

# --- CRITICAL FIX: Direct Route Imports ---
# Import route modules directly to execute the api.add_resource() calls
# The `api` object is global and will register routes as soon as these are imported.
import backend.routes.appointment_routes
import backend.routes.doctor_routes
import backend.routes.patient_routes
import backend.routes.service_routes

def create_app(config_name='default'):
    """Application factory function."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    # Initialize Flask-RESTful Api instance
    api.init_app(app) # The API is now bound to the app

    # Simple health check/base route
    @app.route('/')
    def index():
        return "Clinic Appointment API is running!"

    return app

if __name__ == '__main__':
    # Use 'development' config by default
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app.run(port=5000)