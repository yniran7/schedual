import json
import requests
from datetime import datetime
from utils import print_resp_stream

event_text = "meeting with tom tomorrow at 6pm to 7pm in the gym, hard training session"

model = 'llama2-uncensored'
model_generate_url = 'http://localhost:11434/api/generate'

template = {
    "name": "",
    "start_datetime": "",
    "end_datetime": "",
    "location": "",
    "description": ""
}



def generate(prompt, context=[]):
    r = requests.post(model_generate_url,
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                          "format": 'json'
                      },
                      stream=True)
    r.raise_for_status()
    print_resp_stream(r)
    

context = generate(f'Extract JSON events from the following text, the time now:{datetime.now()} \nUse the following template: {json.dumps(template)}\ntext: {event_text}')