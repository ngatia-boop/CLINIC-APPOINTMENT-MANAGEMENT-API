# backend/app/api/v1/users/routes.py
# This file defines user routes (list doctors, etc.).

from flask_jwt_extended import jwt_required  # For JWT protection
from app.schemas import users_schema  # Import users schema
from app.repositories import UserRepository  # Import user repository
from app.utils import create_response  # Import response helper
from . import users_bp  # Import users blueprint

@users_bp.route('/doctors', methods=['GET'])
@jwt_required()  # Require authentication
def get_doctors():
    """
    Get all doctors.
    """
    doctors = UserRepository.get_all()  # Get all users
    doctors = [user for user in doctors if user.role == 'doctor']  # Filter doctors
    result = users_schema.dump(doctors)  # Serialize doctors
    return create_response(data=result)
