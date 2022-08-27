import os

# server configure
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("HOST", 8001)
QUEUE_URL = os.environ.get("QUEUE_URL", "amqp://dispatching_queue")
QUEUE_NAME = os.environ.get("QUEUE_NAME", "events")
DATABASE = os.environ.get("DATABASE", "database")
