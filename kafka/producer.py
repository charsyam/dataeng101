from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(100):
    producer.send("test", b'some_message_bytes :{}'.format(i))

producer.flush()
