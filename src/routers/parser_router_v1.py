from fastapi import APIRouter, HTTPException
from src.parsers.parser_v1 import ParserV1
from src.models import ParserRequest, ParserResponse, BaseEvent
from src.settings.config import base_url, api_key, model_name
from pydantic import TypeAdapter

router = APIRouter()

parser_config = {
    'base_url': base_url,
    'api_key': api_key,
    'model_name': model_name
}

parser = ParserV1(config=parser_config)

event_json_schema = {
    "type":"json_schema",
    "json_schema":{
        "name":"events",
        "schema":{
        "type":"object",
            "properties":{
                "events":{
                    "type":"array",
                    "items": TypeAdapter(BaseEvent).json_schema(),
                    "minItems":1
                    }
                }
            }
        }
}

@router.post('/parse-event', response_model=ParserResponse)
async def parse(body: ParserRequest):
    try:
        response = parser.parse(body.event_txt, event_json_schema)
        
        return response
    
    except Exception as err: 
        raise HTTPException(status_code=500, detail=f'Something went wrong: {err}')