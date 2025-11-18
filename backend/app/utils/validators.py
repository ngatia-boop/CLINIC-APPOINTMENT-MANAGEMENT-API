# backend/app/utils/validators.py
# This file contains custom validation utilities.

from marshmallow import ValidationError  # For validation errors
import re  # For regex

def validate_email(email):
    """
    Validate email format.

    Args:
        email: Email string

    Raises:
        ValidationError: If email is invalid
    """
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValidationError('Invalid email format')

def validate_phone(phone):
    """
    Validate phone number format (basic validation).

    Args:
        phone: Phone string

    Raises:
        ValidationError: If phone is invalid
    """
    phone_regex = r'^\+?1?[-.\s]?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})$'
    if phone and not re.match(phone_regex, phone):
        raise ValidationError('Invalid phone number format')

def validate_future_date(date):
    """
    Validate that a date is in the future.

    Args:
        date: Datetime object

    Raises:
        ValidationError: If date is not in the future
    """
    from datetime import datetime
    if date <= datetime.utcnow():
        raise ValidationError('Appointment date must be in the future')
