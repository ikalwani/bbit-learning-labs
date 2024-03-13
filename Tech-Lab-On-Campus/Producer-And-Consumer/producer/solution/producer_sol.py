import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key, exchange_name) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        self.setupRMQConnection()

    def setupRMQConnection():
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)

        # Establish Channel
        channel = connection.channel()

        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange=self.exchange_name)
    
    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        channel.basic_publish(
            exchange= self.exchange_name,
            routing_key= self.routing_key,
            body="Message",
        )

        # Close Channel
        channel.close()

        # Close Connection
        connection.close()