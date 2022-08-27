import pika
import config


class Consumer():

    def __init__(self):
        self.params = pika.URLParameters(config.QUEUE_URL)
        self.connection = None
        self._init_queue()

    def _init_queue(self):
        if not self.connection:
            self.connection = pika.BlockingConnection(self.params)
        self.channel = self.connection.channel() # start a channel
        self.channel.queue_declare(queue=config.QUEUE_NAME) # Declare a queue

    def get_msg(self, callback):
        if not self.channel:
            self._init_queue()
        self.channel.basic_consume(config.QUEUE_NAME, callback, auto_ack=True)

        # start consuming (blocks)
        self.channel.start_consuming()




    def publish_msg(self, msg):
        pass