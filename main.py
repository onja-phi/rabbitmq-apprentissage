import pika;
from fastapi import FastAPI

app = FastAPI()

def get_connection():
    return pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )

@app.post("/send")
def send_message(message: str):
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue='test-queue', durable=True)
    channel.basic_publish(exchange='', routing_key='test-queue', body=message)
    connection.close()
    return {"status": "message envoyé", "message": message}