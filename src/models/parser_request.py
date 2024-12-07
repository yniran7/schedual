from pydantic import BaseModel

class ParserRequest(BaseModel):
    event_txt: str
    