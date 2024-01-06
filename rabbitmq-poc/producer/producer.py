#!/usr/bin/python

import pika
import uuid
import random
from datetime import datetime
import pytz
import json

def get_transaction(): 
    amount = "{:.2f}".format(random.uniform(5.5, 75.5)) 
    now = datetime.now(pytz.timezone('America/Sao_Paulo'))
    date_time = now.strftime("%m/%d/%Y %H:%M:%S")

    return {
        'id': str(uuid.uuid4()),
        'amount': amount,
        'type': 'CREDIT',
        'date_time': date_time
    }


transaction_as_string = json.dumps(get_transaction())


# Creates connection with rabbitmq localhost server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='transactions')

channel.basic_publish(exchange='',
                      routing_key='transactions',
                      body=transaction_as_string)
print(" [x] Send transaction ")
print(transaction_as_string)

connection.close()