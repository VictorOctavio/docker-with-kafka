from flask import Flask, render_template
from kafka import KafkaConsumer
import json

app = Flask(__name__)

consumer = KafkaConsumer(
    'inventory_updates',
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

inventory = {}

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

if __name__ == '__main__':
    for message in consumer:
        inventory_update = message.value
        product_id = inventory_update['product_id']
        quantity = inventory_update['quantity']
        inventory[product_id] = quantity