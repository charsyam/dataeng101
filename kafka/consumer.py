from kafka import KafkaConsumer
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
consumer.subscribe(['test'])
for msg in consumer:
    print(msg)
    print(msg.topic, msg.value)
