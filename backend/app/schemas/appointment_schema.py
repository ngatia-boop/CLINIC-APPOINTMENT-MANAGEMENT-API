# backend/app/schemas/appointment_schema.py
# This file defines Marshmallow schemas for Appointment serialization and validation.

from ..extensions import ma  # Import Marshmallow instance
from ..models import Appointment  # Import Appointment model
from marshmallow import fields, validate  # Import fields and validation

class AppointmentSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for Appointment model serialization and deserialization.
    """
    class Meta:
        model = Appointment  # Link to Appointment model
        load_instance = True  # Allow loading instances

    # Custom fields for related data
    user = fields.Nested('UserSchema', exclude=('password_hash',), dump_only=True)  # Nested user info
    doctor = fields.Nested('UserSchema', exclude=('password_hash',), dump_only=True)  # Nested doctor info

    # Validation
    appointment_date = fields.DateTime(required=True)  # Required date field
    status = fields.Str(validate=validate.OneOf(['scheduled', 'completed', 'cancelled']))  # Valid statuses

# Schema instances
appointment_schema = AppointmentSchema()  # Single appointment schema
appointments_schema = AppointmentSchema(many=True)  # Multiple appointments schema
