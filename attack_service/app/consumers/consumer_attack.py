from confluent_kafka import Consumer
from utils.logger import log_event
from schemas.attack_schema import AttackSignal
from services.attack_service import Processor
import logging
import json
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)


kafka_host = os.getenv("KAFKA_HOST")
kafka_port = int(os.getenv("KAFKA_PORT"))



class ConsumerCon:

    
    @staticmethod
    def create_consumer():
        config = {
                    "bootstrap.servers":f"{kafka_host}:{kafka_port}",
                    "group.id": "attack",
                    "auto.offset.reset": "earliest"
                    }
        return Consumer(config)
    

    @staticmethod
    def handle_message(msg):
        value = msg.value().decode("utf-8")
        data = json.loads(value)
        logger.info("data %s", data)
        signal = AttackSignal(**data)
        logger.info("Valid signal %s", signal)
        Processor.process(signal)




    @staticmethod
    def consumer_loop():
        consumer = ConsumerCon.create_consumer()
        consumer.subscribe(["attack"])
        try:
            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    logger.error("ERROR: %s", msg.error())
                    log_event("ERROR", msg.error())
                    continue

            
                ConsumerCon.handle_message(msg)
        finally:
            consumer.close()