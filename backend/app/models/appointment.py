# backend/app/models/appointment.py
# This file defines the Appointment model using SQLAlchemy.
# It represents appointments between patients and doctors.

from ..extensions import db  # Import the database instance
from datetime import datetime, timezone  # For timestamps

class Appointment(db.Model):
    """
    Appointment model for storing appointment details.
    """
    __tablename__ = 'appointments'  # Table name in the database

    id = db.Column(db.Integer, primary_key=True)  # Primary key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User
    doctor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to User (doctor)
    appointment_date = db.Column(db.DateTime, nullable=False)  # Date and time of appointment
    status = db.Column(db.String(20), nullable=False, default='scheduled')  # Status: scheduled, completed, cancelled
    notes = db.Column(db.Text)  # Additional notes
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Creation timestamp
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # Update timestamp

    def __repr__(self):
        """
        String representation of the Appointment object.
        """
        return f'<Appointment {self.id} - {self.status}>'
