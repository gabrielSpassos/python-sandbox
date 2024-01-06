# Python RabbitMQ Simple POC

### Usage

* Execute RabbitMQ
```shell
docker-compose up
```

* Access the RabbitMQ interface on http://localhost:15672/
> User: guest

> Password: guest

* Install dependencies (producer/consumer)
```shell
pip3 install -r requirements.txt
```

* Execute project
```shell
docker-compose up
```

-----

Commands to run manually:

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