from kafka import KafkaProducer


class Kafka_send():
    def __init__(self, host, port, topic, message):
        self.host = host
        self.port = port
        self.topic = topic
        self.message = str(message).encode('utf-8')
        self.producer = KafkaProducer(bootstrap_servers=["192.168.1.133:9092"])

    def sendmessage(self, info):
        self.producer.send('lmt', str(info).encode('utf-8'))


if __name__ == '__main__':
    kafka = Kafka_send('192.168.1.1', 9092, 'lmt', 'Hello world')
    kafka.sendmessage()
