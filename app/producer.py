from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

TOPIC_NAME = 'inventory_updates'

def send_inventory_update(product_id, quantity):
    message = {'product_id': product_id, 'quantity': quantity}
    producer.send(TOPIC_NAME, message)
    producer.flush()

# use example
send_inventory_update(1, 10)
