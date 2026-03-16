from confluent_kafka import Producer
import json
import os


kafka_host = os.getenv("KAFKA_HOST")
kafka_port = int(os.getenv("KAFKA_PORT"))


class ProducerConn:

    @staticmethod
    def create_producer():
        config = {
            "bootstrap.servers":f"{kafka_host}:{kafka_port}"
        }
        return Producer(config)
    
    @staticmethod
    def send_event_to_kafka(event: dict):
        producer = ProducerConn.create_producer()
        value = json.dumps(event)
        producer.produce(
            topic="intel_signals_dlq",
            value=value
        )
        return
