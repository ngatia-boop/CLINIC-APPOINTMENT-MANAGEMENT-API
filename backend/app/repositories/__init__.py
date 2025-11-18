# backend/app/repositories/__init__.py
# This file imports all repositories to make them available when importing the repositories package.

from .user_repository import UserRepository  # Import user repository
from .appointment_repository import AppointmentRepository  # Import appointment repository

# Add more repository imports here as they are created
