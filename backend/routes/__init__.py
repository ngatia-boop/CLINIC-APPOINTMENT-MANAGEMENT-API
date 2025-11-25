# backend/routes/__init__.py
from flask import Blueprint

patients_bp = Blueprint("patients", __name__)
doctors_bp = Blueprint("doctors", __name__)
appointments_bp = Blueprint("appointments", __name__)

# Import routes to register them with blueprints
from routes import appointment_routes
from routes import doctor_routes
from routes import patient_routes