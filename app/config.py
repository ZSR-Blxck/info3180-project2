import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')or 'postgresql://username:password@localhost/databasename'

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

    UPLOAD_FOLDER ='./app/static/uploads'
    PROFILE_IMG_UPLOAD_FOLDER = os.path.join("static/uploads", "profile_photos")
    CARS_UPLOAD_FOLDER = os.path.join("static/uploads", "cars")

    db = SQLAlchemy(app)