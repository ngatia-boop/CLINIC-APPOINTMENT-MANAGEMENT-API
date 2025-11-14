import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://njagua:mypassword@localhost:5432/clinic_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
