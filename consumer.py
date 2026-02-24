from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'orders-consumer-v1',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['orders'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        print("Waiting for messages...")
        continue

    if msg.error():
        print("Consumer error:", msg.error())
        continue

    value = msg.value().decode("utf-8")
    order = json.loads(value)

    print(order["order_id"], order["item"], order["user"])
    if order["item"] == "Laptop":
        print("Laptop order received for user:", order["user"])