import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='test-queue', durable=True)

def callback(ch, method, properties, body):
    print(f"Message reçu : {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue='test-queue',
    on_message_callback=callback,
    auto_ack=False
)

print("En attente de messages...")
channel.start_consuming()