#!/usr/bin/python

import requests

my_data = {
    'key': 'value'
}

response = requests.request(
    method='get',
    url='http://get-with-body-poc.free.beeceptor.com/get-with-body-poc',
    data=my_data,
    json=my_data,
    headers={'content-type':'application/json'})

print(response.status_code);
print(response.headers);
print(response.text);