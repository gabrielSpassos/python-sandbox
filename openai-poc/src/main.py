#!/usr/bin/python

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

openai_key = os.getenv("openai_key")

client = OpenAI(api_key=openai_key)

response = client.responses.create(
    model = "gpt-4.1-nano",
    input = "Give me tips where to go at Buenos Aires on a trip with 5 nights and 6 days."
)

print(response.output_text)
