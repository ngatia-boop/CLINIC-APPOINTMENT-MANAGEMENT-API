# backend/app/schemas/user_schema.py
# This file defines Marshmallow schemas for User serialization and validation.

from ..extensions import ma  # Import Marshmallow instance
from ..models import User  # Import User model
from marshmallow import fields, validate, ValidationError, validates_schema  # Import fields and validation

class UserSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for User model serialization and deserialization.
    """
    class Meta:
        model = User  # Link to User model
        load_instance = True  # Allow loading instances
        exclude = ('password_hash',)  # Exclude password hash from serialization

    # Custom fields
    password = fields.Str(required=True, validate=validate.Length(min=6), load_only=True)  # Password field for input only
    confirm_password = fields.Str(load_only=True)  # Confirm password for registration

    # Validation
    @validates_schema
    def validate_passwords(self, data, **kwargs):
        """
        Validate that password and confirm_password match.
        """
        if 'password' in data and 'confirm_password' in data:
            if data['password'] != data['confirm_password']:
                raise ValidationError('Passwords do not match')

# Schema instances
user_schema = UserSchema()  # Single user schema
users_schema = UserSchema(many=True)  # Multiple users schema
