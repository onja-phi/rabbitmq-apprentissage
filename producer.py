import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test-queue', durable=True)

channel.basic_publish(
    exchange='',
    routing_key='test-queue',
    body='Hello World! depuis Python'
)

print("Message envoyé!")
connection.close()