# backend/models.py

from datetime import datetime
from .extensions import db
from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint

# Association Table for Doctor <-> Service (Many-to-Many)
DoctorService = db.Table('doctor_services',
    db.Column('doctor_id', db.Integer, db.ForeignKey('doctors.id'), primary_key=True),
    db.Column('service_id', db.Integer, db.ForeignKey('services.id'), primary_key=True)
)

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Email must contain '@'")
        return email

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)
    
    # Many-to-Many relationship with Service
    services = db.relationship('Service', secondary=DoctorService, backref=db.backref('doctors', lazy='dynamic'))
    
class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False) # e.g., 30, 60
    price = db.Column(db.Float, nullable=False)

    __table_args__ = (
        CheckConstraint('duration_minutes > 0', name='check_duration_positive'),
    )

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False) # Calculated based on start_time and service duration
    status = db.Column(db.String(50), default='Scheduled', nullable=False) # Scheduled, Completed, Cancelled
    
    service = db.relationship('Service', backref='appointments', lazy=True)

    __table_args__ = (
        CheckConstraint('start_time < end_time', name='check_start_before_end'),
    )

    @validates('status')
    def validate_status(self, key, status):
        valid_statuses = ['Scheduled', 'Completed', 'Cancelled']
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return status