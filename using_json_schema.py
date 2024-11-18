from openai import OpenAI
import json
from datetime import datetime
from config import base_url, api_key, model_name
from event_schema import event_schema

event_text = "I have a meeting tomorrow at 6pm for an hour with Tom Koren and Tal Dokhnian in the gym, we are going to talk about life"

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

messages = [
    {"role": "system", "content": f'todays date and time is: {datetime.now()}'},
    {"role": "system", "content": "You are a helpful AI assistant that can read messages and create events from them."},
    {"role": "user", "content": f'create an event from this: {event_text}'}
]


response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    response_format=event_schema,
)

results = json.loads(response.choices[0].message.content)
print(json.dumps(results, indent=2))
