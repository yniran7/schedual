from dataclasses import dataclass

@dataclass
class Reminder:
    id: str
    """ 1: email, 2: popup """
    method: int
    minutes: int