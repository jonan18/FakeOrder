from os import environ

from dotenv import load_dotenv

# Only needed for developing, on production Docker .env file is used
load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""
    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///monolithic.db?check_same_thread=False"
    SQLALCHEMY_TRACK_MODIFICATIONS = "False"
    CLIENT_IP = environ.get("CLIENT_IP")
    GUNICORN_PORT = environ.get("GUNICORN_PORT")


class TestingConfig(Config):
    """" Configurating for testing , with a separate test database"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    DEBUG = True

