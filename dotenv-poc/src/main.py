#!/usr/bin/python

from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("openai_key")
print(f"open ai key: {openai_key}")

key2 = os.getenv("key2")
print(f"key2: {key2}")