from flask import Flask
from flask_cors import CORS
from backend.extensions import db

def create_app():
    app = Flask(__name__)

    # Configure SQLAlchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinic.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Import and register Blueprints
    from backend.routes.patient_routes import patients_bp
    from backend.routes.doctor_routes import doctors_bp
    from backend.routes.appointment_routes import appointments_bp

    app.register_blueprint(patients_bp, url_prefix="/patients")
    app.register_blueprint(doctors_bp, url_prefix="/doctors")
    app.register_blueprint(appointments_bp, url_prefix="/appointments")

    # Create tables
    with app.app_context():
        from backend.models import Patient, Doctor, Appointment
        db.create_all()

    return app
