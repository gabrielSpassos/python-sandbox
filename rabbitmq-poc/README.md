# Python RabbitMQ Simple POC

### Usage

* Execute RabbitMQ
```shell
docker-compose up
```

* Access the RabbitMQ interface on http://localhost:15672/
> User: guest

> Password: guest

* Execute project
```shell
docker-compose up
```

* How looks like the exchange (producer)
![Captura de tela 2024-01-07 160436](https://github.com/gabrielSpassos/python-sandbox/assets/32275521/e6f2bb80-d22a-4db4-aea9-9d804fe15cba)

* Debit consumer ('DEBIT' as routing key)
![Captura de tela 2024-01-07 160514](https://github.com/gabrielSpassos/python-sandbox/assets/32275521/bb44ab9f-cd8b-47c8-ad68-8e6d28ac371f)

* Credit consumer ('CREDIT' as routing key)
![Captura de tela 2024-01-07 160528](https://github.com/gabrielSpassos/python-sandbox/assets/32275521/3907e589-cdd2-4a55-b8a0-c8a40551b6c1)
  
-----

Commands to run manually:

* Install dependencies (producer/consumer)
```shell
pip3 install -r requirements.txt
```

* Run Producer
```shell
python3 producer/producer.py
```

* Run Consumer
```shell
python3 consumer/consumer.py
```

* Build Producer Docker container
```shell
docker build -t rabbitmq-producer .
```

* Execute Producer Docker container
```shell
docker run --name rabbitmq-producer rabbitmq-producer
```

* Build Consumer Docker container
```shell
docker build -t rabbitmq-consumer .
```

* Execute Consumer Docker container
```shell
docker run --name rabbitmq-consumer rabbitmq-consumer
```
