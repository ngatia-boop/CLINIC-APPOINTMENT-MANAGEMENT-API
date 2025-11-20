# backend/app/services/appointment_service.py
# This file contains business logic for appointment services.

from ..models import Appointment, User  # Import models
from ..extensions import db  # Import database instance
from werkzeug.exceptions import BadRequest, NotFound  # For error handling
from datetime import datetime  # For date handling

class AppointmentService:
    """
    Service class for appointment-related operations.
    """

    @staticmethod
    def create_appointment(user_id, doctor_id, appointment_date, notes=None):
        """
        Create a new appointment.

        Args:
            user_id: ID of the patient
            doctor_id: ID of the doctor
            appointment_date: Date and time of appointment
            notes: Optional notes

        Returns:
            Appointment object

        Raises:
            BadRequest: If doctor is not found or invalid
            NotFound: If user is not found
        """
        # Validate user and doctor
        user = db.session.get(User, user_id)
        if not user:
            raise NotFound('User not found')

        doctor = db.session.get(User, doctor_id)
        if not doctor or doctor.role != 'doctor':
            raise BadRequest('Invalid doctor')

        # Check for scheduling conflicts (basic check)
        existing = Appointment.query.filter_by(
            doctor_id=doctor_id,
            appointment_date=appointment_date
        ).first()
        if existing:
            raise BadRequest('Doctor is not available at this time')

        # Create appointment
        appointment = Appointment(
            user_id=user_id,
            doctor_id=doctor_id,
            appointment_date=appointment_date,
            notes=notes
        )

        db.session.add(appointment)
        db.session.commit()

        return appointment

    @staticmethod
    def get_user_appointments(user_id):
        """
        Get all appointments for a user.

        Args:
            user_id: User ID

        Returns:
            List of appointments
        """
        return Appointment.query.filter_by(user_id=user_id).all()

    @staticmethod
    def update_appointment_status(appointment_id, status):
        """
        Update the status of an appointment.

        Args:
            appointment_id: Appointment ID
            status: New status

        Returns:
            Updated appointment

        Raises:
            NotFound: If appointment not found
        """
        appointment = db.session.get(Appointment, appointment_id)
        if not appointment:
            raise NotFound('Appointment not found')

        appointment.status = status
        db.session.commit()

        return appointment
