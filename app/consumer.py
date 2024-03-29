from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'inventory_updates',
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for meesage in consumer:
    print(f"Received message: {meesage.value}")
    