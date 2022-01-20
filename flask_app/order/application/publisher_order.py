"""
import ssl
import pika
from . import Config

# solves the following: https://stackoverflow.com/questions/28768530/certificateerror-hostname-doesnt-match
ssl.match_hostname = lambda cert, hostname: True


def publish_msg(exchange, routing_key, message):
    ssl_options = set_ssl()

    credentials = pika.PlainCredentials(username='rabbitmq', password='rabbitmq')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            ssl_options=ssl_options,
            host=Config.RABBITMQ_IP, port=5671, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    channel.basic_publish(
        exchange=exchange, routing_key=routing_key, body=message)
    print(" [x] Sent %r:%r" % (routing_key, message))
    connection.close()


def set_ssl():
    context = ssl.create_default_context(
        cafile=Config.CA_CERTS)
    context.load_cert_chain(Config.CERT_FILE,
                            Config.KEY_FILE)
    ssl_options = pika.SSLOptions(context, Config.RABBITMQ_IP)
    return ssl_options """
