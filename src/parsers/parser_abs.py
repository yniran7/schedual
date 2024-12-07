from abc import ABC, abstractmethod

class EventParser(ABC):
    
    @abstractmethod
    def __init__(self, config):
        # TODO: add config type
        self.config = config
    
    @abstractmethod
    def parse(self, event_text, options = {}):
        pass