# backend/main.py
import os
from flask import Flask, jsonify
from flask_cors import CORS
from .extensions import db
from .routes import appointments_bp, doctors_bp, patients_bp

def create_app():
    app = Flask(__name__)
    
    # Configure CORS - Allow requests from your frontend
    CORS(app, resources={
        r"/*": {
            "origins": os.getenv("CORS_ORIGINS", "*").split(","),
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///clinic.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(appointments_bp, url_prefix='/api/appointments')
    app.register_blueprint(doctors_bp, url_prefix='/api/doctors')
    app.register_blueprint(patients_bp, url_prefix='/api/patients')
    
    # Health check endpoints
    @app.route('/')
    def home():
        return jsonify({
            "message": "Clinic Management API is running!",
            "status": "success",
            "version": "1.0.0",
            "endpoints": {
                "appointments": "/api/appointments",
                "doctors": "/api/doctors",
                "patients": "/api/patients"
            }
        })
    
    @app.route('/api/health')
    def health():
        return jsonify({
            "status": "healthy",
            "service": "Clinic Management Backend",
            "database": "connected" if check_database() else "disconnected"
        })
    
    def check_database():
        """Check if database connection is working"""
        try:
            # Try to execute a simple query
            db.session.execute('SELECT 1')
            return True
        except Exception:
            return False
    
    return app

app = create_app()

if __name__ == '__main__':
    # Get port from environment variable (Render provides this)
    port = int(os.getenv('PORT', 5000))
    # Use 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=port, debug=False) 