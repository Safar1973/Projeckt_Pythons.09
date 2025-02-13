from abc import ABC, abstractmethod

class IController(ABC):
    @abstractmethod
    def handle_request(self, action):
        pass
