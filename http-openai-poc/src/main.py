#!/usr/bin/python

from dotenv import load_dotenv
import os
import requests

load_dotenv()

openai_key = os.getenv("openai_key")
url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Authorization': f'Bearer {openai_key}',
    'Content-Type': 'application/json'
}

data = {
    "model": "gpt-4.1-nano",
    "messages": [
        {"role": "user", "content": "Dicas de onde ir em Buenos Aires numa viagem de 5 noites e 6 dias."}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    json_response = response.json()
    print(json_response['choices'][0]['message']['content'])
else:
    print("Error to call openAI via HTTP request:", response.status_code)
    print(response.text)
