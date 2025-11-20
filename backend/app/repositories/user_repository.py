# backend/app/repositories/user_repository.py
# This file contains data access logic for User entities.

from ..models import User  # Import User model
from ..extensions import db  # Import database instance

class UserRepository:
    """
    Repository class for User data access.
    """

    @staticmethod
    def get_by_id(user_id):
        """
        Get user by ID.

        Args:
            user_id: User ID

        Returns:
            User object or None
        """
        return db.session.get(User, user_id)

    @staticmethod
    def get_by_username(username):
        """
        Get user by username.

        Args:
            username: Username

        Returns:
            User object or None
        """
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email):
        """
        Get user by email.

        Args:
            email: Email address

        Returns:
            User object or None
        """
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_all():
        """
        Get all users.

        Returns:
            List of User objects
        """
        return User.query.all()

    @staticmethod
    def create(user):
        """
        Create a new user.

        Args:
            user: User object to save
        """
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update(user):
        """
        Update an existing user.

        Args:
            user: User object to update
        """
        db.session.commit()

    @staticmethod
    def delete(user):
        """
        Delete a user.

        Args:
            user: User object to delete
        """
        db.session.delete(user)
        db.session.commit()
