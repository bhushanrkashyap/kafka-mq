from confluent_kafka import Producer
import json

p = Producer({'bootstrap.servers': 'localhost:9092'})

order1= {
    "order_id": 1001,
    "item": "Phone",
    "user": "Bhushan"
}
order = {
    "order_id": 1002,
    "item": "Laptop",
    "user": "Alice"
}

x = [order1 , order]
for order in x:
    p.produce("orders", value=json.dumps(order))
    print("Order produced:", order)
p.flush()
