# backend/app/models/user.py
# This file defines the User model using SQLAlchemy.
# It represents users in the clinic system (doctors, patients, admins).

from ..extensions import db  # Import the database instance
from werkzeug.security import generate_password_hash, check_password_hash  # For password hashing
from datetime import datetime, timezone  # For timestamps

class User(db.Model):
    """
    User model for storing user information.
    """
    __tablename__ = 'users'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    username = db.Column(db.String(80), unique=True, nullable=False)  # Unique username
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    role = db.Column(db.String(20), nullable=False, default='patient')  # Role: patient, doctor, admin
    first_name = db.Column(db.String(50), nullable=False)  # First name
    last_name = db.Column(db.String(50), nullable=False)  # Last name
    phone = db.Column(db.String(20))  # Phone number
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Creation timestamp
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Update timestamp

    # Relationships
    appointments = db.relationship('Appointment', backref='user', lazy=True, foreign_keys='Appointment.user_id')  # One-to-many with appointments as patient
    doctor_appointments = db.relationship('Appointment', backref='doctor', lazy=True, foreign_keys='Appointment.doctor_id')  # One-to-many with appointments as doctor

    def set_password(self, password):
        """
        Hash and set the password.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if the provided password matches the hashed password.
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        """
        String representation of the User object.
        """
        return f'<User {self.username}>'
