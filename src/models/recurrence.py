from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Recurrence:
    id: str
    frequency: str
    interval: str
    count: int
    until: datetime
    by: str
    exception: List[datetime]