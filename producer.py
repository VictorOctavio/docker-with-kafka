from kafka import KafkaProducer
import json

if __name__ == '__main__':
    print("Starting kafka producer..")
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    # Topic, Value
    producer.send("orders", "order 3")
    producer.flush()
    print("message produced successfully")
    