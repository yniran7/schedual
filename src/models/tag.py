from dataclasses import dataclass

@dataclass
class Tag:
    id: str
    description: str
    title: str
    color: str
    background_color: str