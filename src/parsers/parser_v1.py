from openai import OpenAI
import json
from datetime import datetime
from .parser_abs import EventParser

class ParserV1(EventParser):
    
    client: OpenAI
    
    def __init__(self, config):
        super().__init__(config)
        
        self.client = OpenAI(
            base_url = config['base_url'],
            api_key = config['api_key']
        )
    
    def parse(self, event_text, response_format, options={}):
        messages = self.__generate_messages(event_text)
        
        response = self.__get_model_response(messages, response_format, options)

        results = json.loads(response.choices[0].message.content)

        return results
    
    def __generate_messages(self, event_text):
        return [
            {"role": "system", "content": f"""Nows date and time is: {datetime.now()}, timezone +03:00.
            You are a helpful AI assistant that can read messages and create events from them."""},
            {"role": "user", "content": f'create an event from this: {event_text}'}
        ]
        
    def __get_model_response(self, messages, response_format, options):
        
        # TODO: find a cleaner way of doing this
        
        return self.client.chat.completions.create(
            model=self.config['model_name'] if('model_name' not in options) else options['model_name'],
            messages=messages,
            response_format=response_format,
            temperature= 0.3 if('temperature' not in options) else options['temperature'],
            top_p=0.5 if('top_p' not in options) else options['top_p'],
        )
        
   


