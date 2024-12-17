from rocketmq.client import Producer, Message
from app.config import settings

producer = None

async def init_mq():
    global producer
    producer = Producer("ExampleProducer")
    producer.set_name_server_address(settings.rocketmq_endpoint)
    producer.start()
    print("RocketMQ Producer initialized")

