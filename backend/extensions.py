from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()
api = Api(prefix="/api")  # All routes will automatically be under /api
