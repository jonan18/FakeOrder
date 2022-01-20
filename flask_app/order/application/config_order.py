from os import environ

from dotenv import load_dotenv

# Only needed for developing, on production Docker .env file is used
load_dotenv()


class Config:
    """Set Flask configuration vars from .env file."""
    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///monolithic.db?check_same_thread=False"
    SQLALCHEMY_TRACK_MODIFICATIONS = "False"
    DELIVERY_IP = environ.get("DELIVERY_IP")
    MACHINE_IP = environ.get("MACHINE_IP")
    PAYMENT_IP = environ.get("PAYMENT_IP")
    CLIENT_IP = environ.get("CLIENT_IP")

    GUNICORN_PORT = environ.get("GUNICORN_PORT")
    # print(SQLALCHEMY_DATABASE_URI)

    """ Set RabbitMQ env vars """

    #RABBITMQ_IP = environ.get("RABBITMQ_IP")
    #RABBITMQ_USER = environ.get("RABBITMQ_USER")
    #RABBITMQ_PASS = environ.get("RABBITMQ_PASS")

    #CA_CERTS = environ.get("RABBITMQ_CA_CERT")
    #KEY_FILE = environ.get("RABBITMQ_CLIENT_KEY")
    #CERT_FILE = environ.get("RABBITMQ_CLIENT_CERT")
