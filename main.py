import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("ANTHROPIC_API_KEY")
ENDPOINT = "https://api.anthropic.com/v1/messages"
HEADERS = {
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}

def make_request(message):
    payload = {
        "model": "claude-sonnet-4-6",
        "max_tokens": 256,
        "temperature": 0.5,
        "system": "You are a helpful assistant.",
        "messages": [{"role": "user", "content": message}]
    }
    return requests.post(ENDPOINT, headers=HEADERS, json=payload)

def extract_reply(response):
    if response.status_code == 200:
        return response.json()["content"][0]["text"]
    return None

response = make_request("What is the capital of France?")

print(f"Status Code : {response.status_code}")
response_data = response.json()
print(f"Response    :\n{json.dumps(response_data, indent=2)}")

reply = extract_reply(response)
if reply:
    print(f"\nClaude says: {reply}")

second_response = make_request("What is 2+2?")
second_reply = extract_reply(second_response)
if second_reply:
    print(f"\nSecond answer: {second_reply}")
