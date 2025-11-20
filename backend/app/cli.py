# backend/app/cli.py
# This file defines custom Flask CLI commands.

import click  # For CLI commands
from .extensions import db  # Import database
from .models import User  # Import User model

def register_commands(app):
    """
    Register custom CLI commands with the app.

    Args:
        app: Flask app instance
    """
    @app.cli.command('create-admin')
    @click.argument('username')
    @click.argument('email')
    @click.argument('password')
    def create_admin(username, email, password):
        """
        Create an admin user.
        """
        if User.query.filter_by(username=username).first():
            click.echo('Username already exists')
            return

        user = User(
            username=username,
            email=email,
            first_name='Admin',
            last_name='User',
            role='admin'
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        click.echo(f'Admin user {username} created')

    @app.cli.command('seed-doctors')
    def seed_doctors():
        """
        Seed the database with sample doctors.
        """
        doctors = [
            {'username': 'dr_smith', 'email': 'smith@clinic.com', 'first_name': 'John', 'last_name': 'Smith'},
            {'username': 'dr_jones', 'email': 'jones@clinic.com', 'first_name': 'Jane', 'last_name': 'Jones'},
        ]

        for doc_data in doctors:
            if not User.query.filter_by(username=doc_data['username']).first():
                user = User(
                    username=doc_data['username'],
                    email=doc_data['email'],
                    first_name=doc_data['first_name'],
                    last_name=doc_data['last_name'],
                    role='doctor'
                )
                user.set_password('password123')  # Default password
                db.session.add(user)

        db.session.commit()
        click.echo('Doctors seeded')
