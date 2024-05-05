import pika
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# RabbitMQ'ya bağlanma
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='payment_queue')

def process_payment_request(payment_data):

    channel.basic_publish(exchange='', routing_key='payment_queue', body=json.dumps(payment_data))
    print("Payment request processed and sent to payment queue.")

@app.route('/make_payment', methods=['POST'])
def make_payment():
    payment_data = request.json
    process_payment_request(payment_data)
    return jsonify({"message": "Payment request received and being processed."}), 200

def process_payment(payment_data):

    print("Payment processed successfully for:", payment_data)


# RabbitMQ üzerinden ödeme işlemi alımı
def callback(ch, method, properties, body):
    payment_data = json.loads(body)
    process_payment(payment_data)

channel.basic_consume(queue='payment_queue', on_message_callback=callback, auto_ack=True)
print('Waiting for payment requests...')

if __name__ == "__main__":
    app.run(port=5000)
