from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime
from .reminder import Reminder
from .tag import Tag
from .recurrence import Recurrence

@dataclass
class BaseEvent:
    title: str
    start_time: datetime
    end_time: datetime
    location: str
    description: Optional[str]
    attendees: List[str]
    
    
@dataclass
class Event(BaseEvent):
    id: str
    time_zone: str
    base_event_id: Optional[str]
    recurrence: Optional[Recurrence]
    reminders: List[Reminder]
    Tag: List[Tag]
