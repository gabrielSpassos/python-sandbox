#!/usr/bin/python

import os
import pika
import uuid
import random
from datetime import datetime
import pytz
import json
import time

def get_transaction(): 
    amount = "{:.2f}".format(random.uniform(5.5, 75.5))
    type = 'CREDIT' if random.randint(0, 1) == 1 else 'DEBIT'
    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")

    return {
        'id': str(uuid.uuid4()),
        'amount': amount,
        'type': type,
        'date_time': date_time
    }


def produce_message():
    transaction = get_transaction()
    transaction_as_string = json.dumps(transaction)

    amqp_url = os.environ.get('AMQP_URL', 'amqp://localhost')
    url_params = pika.URLParameters(amqp_url)

    # Creates connection with rabbitmq localhost server
    connection = pika.BlockingConnection(url_params)
    channel = connection.channel()

    channel.exchange_declare(exchange='transactions', exchange_type='topic')

    channel.basic_publish(exchange='transactions', routing_key=transaction["type"], body=transaction_as_string)
    print(" [x] Send transaction ")
    print(transaction_as_string)
    print(" [x] Routing Key ")
    print(transaction["type"])

    channel.close()
    connection.close()


if __name__ == '__main__':
    try:
        while True:
            produce_message()
            time.sleep(10)
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

