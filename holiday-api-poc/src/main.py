#!/usr/bin/python

from dotenv import load_dotenv
import os
import requests

load_dotenv()

holiday_api_key = os.getenv("HOLIDAY_API_SECRET_KEY")
holiday_api_url = 'https://holidays.abstractapi.com'

params = {
    "api_key": holiday_api_key,
    "country": "BR",
    "year": 2025,
    "month": 12,
    "day": 25
}

response = requests.get(f"{holiday_api_url}/v1/", params=params)
print('Response Status:', response.status_code)
print('Response Body:', response.content)
