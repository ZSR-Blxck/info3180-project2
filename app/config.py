import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # load environment variables from .env if it exists.

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://trixgjzhhllmyc:7ebaa008123c00c9f70d5df3a35b204717acd5aeacf813d87e3246292662f27a@ec2-54-80-123-146.compute-1.amazonaws.com:5432/d2qqedn5ugrnoi')or 'postgresql://postgres:admin@localhost/unitedauto'

    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed

    UPLOAD_FOLDER ='./app/static/uploads'
    PROFILE_IMG_UPLOAD_FOLDER = os.path.join("static/uploads", "profile_photos")
    CARS_UPLOAD_FOLDER = os.path.join("static/uploads", "cars")
