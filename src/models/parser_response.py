from pydantic import BaseModel
from dataclasses import dataclass
from typing import List
from .event import BaseEvent

@dataclass
class ParserResponse(BaseModel):
    events: List[BaseEvent]
