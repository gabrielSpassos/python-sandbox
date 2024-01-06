#!/usr/bin/python

import pika
import os


def callback(ch, method, properties, body):
    print(f" [x] Received {body}")


def main():
    amqp_url = os.environ.get('AMQP_URL', 'amqp://localhost')
    url_params = pika.URLParameters(amqp_url)

    # Creates connection with rabbitmq localhost server
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    exchange_name = "transactions"
    transaction_type = os.environ.get('TRANSACTION_TYPE', 'DEBIT')
    queue_name = transaction_type.lower() + "-" + exchange_name
    channel.queue_declare(queue=queue_name)

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=transaction_type)

    channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
