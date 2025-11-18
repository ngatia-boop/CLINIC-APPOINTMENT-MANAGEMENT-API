# backend/app/tests/test_appointments.py
# This file contains tests for appointment functionality.

import pytest  # For testing framework
from datetime import datetime, timedelta, timezone  # For date handling
from ..models import User, Appointment  # Import models
from ..services import AppointmentService  # Import AppointmentService
from ..extensions import db  # Import database

def test_create_appointment(app):
    """
    Test creating an appointment.
    """
    with app.app_context():
        # Create user and doctor
        user = User(username='patient', email='patient@example.com', first_name='Patient', last_name='User')
        user.set_password('password')
        doctor = User(username='doctor', email='doctor@example.com', first_name='Doctor', last_name='User', role='doctor')
        doctor.set_password('password')
        db.session.add(user)
        db.session.add(doctor)
        db.session.commit()

        # Create appointment
        future_date = datetime.now(timezone.utc) + timedelta(days=1)
        appointment = AppointmentService.create_appointment(
            user_id=user.id,
            doctor_id=doctor.id,
            appointment_date=future_date,
            notes='Test appointment'
        )
        assert appointment.user_id == user.id
        assert appointment.doctor_id == doctor.id
        assert appointment.status == 'scheduled'

def test_get_user_appointments(app):
    """
    Test getting user's appointments.
    """
    with app.app_context():
        # Create user and doctor
        user = User(username='patient', email='patient@example.com', first_name='Patient', last_name='User')
        user.set_password('password')
        doctor = User(username='doctor', email='doctor@example.com', first_name='Doctor', last_name='User', role='doctor')
        doctor.set_password('password')
        db.session.add(user)
        db.session.add(doctor)
        db.session.commit()

        # Create appointment
        future_date = datetime.now(timezone.utc) + timedelta(days=1)
        AppointmentService.create_appointment(
            user_id=user.id,
            doctor_id=doctor.id,
            appointment_date=future_date,
            notes='Test appointment'
        )

        # Get appointments
        appointments = AppointmentService.get_user_appointments(user.id)
        assert len(appointments) == 1

def test_update_appointment_status(app):
    """
    Test updating appointment status.
    """
    with app.app_context():
        # Create user and doctor
        user = User(username='patient', email='patient@example.com', first_name='Patient', last_name='User')
        user.set_password('password')
        doctor = User(username='doctor', email='doctor@example.com', first_name='Doctor', last_name='User', role='doctor')
        doctor.set_password('password')
        db.session.add(user)
        db.session.add(doctor)
        db.session.commit()

        # Create appointment
        future_date = datetime.now(timezone.utc) + timedelta(days=1)
        appointment = AppointmentService.create_appointment(
            user_id=user.id,
            doctor_id=doctor.id,
            appointment_date=future_date,
            notes='Test appointment'
        )

        # Update status
        updated = AppointmentService.update_appointment_status(appointment.id, 'confirmed')
        assert updated.status == 'confirmed'
