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

