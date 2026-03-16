from confluent_kafka import Consumer
from utils.logger import log_event
from schemas.intel_schema import IntelSignal
from kafka_producer.dlq_producer import ProducerConn
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
                    "group.id": "intel",
                    "auto.offset.reset": "earliest"
                    }
        return Consumer(config)
    

    @staticmethod
    def handle_message(msg):
        value = msg.value().decode("utf-8")
        data = json.loads(value)
        try:
            signal = IntelSignal(**data)
            logger.info("Valid signal %s", signal)
            log_event("INFO", logger.info("Valid signal %s", signal))
        except Exception as e:
            event = {
                "data": data,
                "error": str(e)
            }
            ProducerConn.send_event_to_kafka(event)



    @staticmethod
    def consumer_loop():
        consumer = ConsumerCon.create_consumer()
        consumer.subscribe(["intel"])
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
            consumer.close
