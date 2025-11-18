# backend/app/repositories/appointment_repository.py
# This file contains data access logic for Appointment entities.

from ..models import Appointment  # Import Appointment model
from ..extensions import db  # Import database instance

class AppointmentRepository:
    """
    Repository class for Appointment data access.
    """

    @staticmethod
    def get_by_id(appointment_id):
        """
        Get appointment by ID.

        Args:
            appointment_id: Appointment ID

        Returns:
            Appointment object or None
        """
        return db.session.get(Appointment, appointment_id)

    @staticmethod
    def get_by_user_id(user_id):
        """
        Get appointments by user ID.

        Args:
            user_id: User ID

        Returns:
            List of Appointment objects
        """
        return Appointment.query.filter_by(user_id=user_id).all()

    @staticmethod
    def get_by_doctor_id(doctor_id):
        """
        Get appointments by doctor ID.

        Args:
            doctor_id: Doctor ID

        Returns:
            List of Appointment objects
        """
        return Appointment.query.filter_by(doctor_id=doctor_id).all()

    @staticmethod
    def get_all():
        """
        Get all appointments.

        Returns:
            List of Appointment objects
        """
        return Appointment.query.all()

    @staticmethod
    def create(appointment):
        """
        Create a new appointment.

        Args:
            appointment: Appointment object to save
        """
        db.session.add(appointment)
        db.session.commit()

    @staticmethod
    def update(appointment):
        """
        Update an existing appointment.

        Args:
            appointment: Appointment object to update
        """
        db.session.commit()

    @staticmethod
    def delete(appointment):
        """
        Delete an appointment.

        Args:
            appointment: Appointment object to delete
        """
        db.session.delete(appointment)
        db.session.commit()
