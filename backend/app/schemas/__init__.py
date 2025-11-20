# backend/app/schemas/__init__.py
# This file imports all schemas to make them available when importing the schemas package.

from .user_schema import user_schema, users_schema  # Import user schemas
from .appointment_schema import appointment_schema, appointments_schema  # Import appointment schemas

# Add more schema imports here as they are created
