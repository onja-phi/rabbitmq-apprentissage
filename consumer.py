import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test-queue', durable=True)

def callback(ch, method, properties, body):
    print(f"Message reçu : {body.decode()}")

channel.basic_consume(
    queue='test-queue',
    on_message_callback=callback,
    auto_ack=True
)

print("En attente de messages...")
channel.start_consuming()