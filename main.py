import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("ANTHROPIC_API_KEY")
ENDPOINT = "https://api.anthropic.com/v1/messages"

def make_request(question):
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 256,
        "temperature": 0.5,
        "system": "You are a helpful assistant.",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }

    response = requests.post(ENDPOINT, headers=headers, json=payload)
    return response

def make_another_request(query):
    headers = {
        "x-api-key": API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 256,
        "temperature": 0.5,
        "system": "You are a helpful assistant.",
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }

    result = requests.post(ENDPOINT, headers=headers, json=payload)
    return result

response = make_request("What is the capital of France?")

print(f"Status Code : {response.status_code}")
response_data = response.json()
print(f"Response    :\n{json.dumps(response_data, indent=2)}")

if response.status_code == 200:
    reply = response.json()["content"][0]["text"]
    print(f"\nClaude says: {reply}")

second_response = make_another_request("What is 2+2?")
if second_response.status_code == 200:
    second_reply = second_response.json()["content"][0]["text"]
    print(f"\nSecond answer: {second_reply}")
