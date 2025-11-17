#backend/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://njagua:mypassword@localhost/clinic_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "super-secret-key"
