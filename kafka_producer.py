from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers='10.142.29.117:9092', api_version=(0, 10))
for _ in range(100):
    producer.send('lex-data', b'some_bytes')

producer.close()
