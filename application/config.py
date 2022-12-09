"""
Flask Config.
"""

from os import environ, path
from dotenv import load_dotenv

# Load .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DEBUG = True
SECRET_KEY = environ.get('SECRET')
PORT = environ.get('PORT')

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

