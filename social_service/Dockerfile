FROM python:3.6
ENV http_proxy http://proxy-chain.xxx.com:911/
ENV https_proxy http://proxy-chain.xxx.com:912/
ENV PYTHONUNBUFFERED 1
RUN mkdir /social_service
WORKDIR /social_service
ADD . /social_service/
RUN pip3 install --upgrade pip3 && \
    pip3 install --no-cache-dir -r requirements.txt