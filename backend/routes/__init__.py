from flask import Flask
from backend.config import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('clinic_backend.config.Config')

    db.init_app(app)

    # Register blueprints
    from backend.routes.patient_routes import patient_bp
    from backend.routes.appointment_routes import appointment_bp

    app.register_blueprint(patient_bp, url_prefix='/patients')
    app.register_blueprint(appointment_bp, url_prefix='/appointments')

    return app
