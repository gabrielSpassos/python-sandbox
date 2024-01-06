# basic python image
FROM python:3.7

# copy the requirements.txt
COPY requirements.txt .

# install pika to access rabbitmq
RUN pip3 install -r requirements.txt

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /usr/src/app/consumer

# copy the file
COPY consumer.py .

# start command
CMD [ "python3", "consumer.py" ]