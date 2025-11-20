# backend/app/api/v1/appointments/routes.py
# This file defines appointment routes (create, list, update).

from flask import request  # For request handling
from flask_jwt_extended import jwt_required  # For JWT protection
from app.schemas import appointment_schema, appointments_schema  # Import schemas
from app.services import AppointmentService  # Import appointment service
from app.utils import create_response, get_current_user  # Import helpers
from . import appointments_bp  # Import appointments blueprint

@appointments_bp.route('', methods=['POST'])
@jwt_required()  # Require authentication
def create_appointment():
    """
    Create a new appointment.
    Expects JSON with doctor_id, appointment_date, notes.
    """
    user = get_current_user()  # Get current user
    data = request.get_json()  # Get JSON data

    try:
        appointment = AppointmentService.create_appointment(
            user_id=user.id,
            doctor_id=data['doctor_id'],
            appointment_date=data['appointment_date'],
            notes=data.get('notes')
        )
        result = appointment_schema.dump(appointment)  # Serialize appointment
        return create_response(data=result, message='Appointment created successfully', status=201)
    except Exception as e:
        return create_response(message=str(e), status=400)

@appointments_bp.route('', methods=['GET'])
@jwt_required()  # Require authentication
def get_appointments():
    """
    Get user's appointments.
    """
    user = get_current_user()  # Get current user
    appointments = AppointmentService.get_user_appointments(user.id)  # Get appointments
    result = appointments_schema.dump(appointments)  # Serialize appointments
    return create_response(data=result)

@appointments_bp.route('/<int:appointment_id>/status', methods=['PUT'])
@jwt_required()  # Require authentication
def update_appointment_status(appointment_id):
    """
    Update appointment status.
    Expects JSON with status.
    """
    data = request.get_json()  # Get JSON data
    status = data.get('status')

    try:
        appointment = AppointmentService.update_appointment_status(appointment_id, status)  # Update status
        result = appointment_schema.dump(appointment)  # Serialize appointment
        return create_response(data=result, message='Appointment status updated')
    except Exception as e:
        return create_response(message=str(e), status=400)
