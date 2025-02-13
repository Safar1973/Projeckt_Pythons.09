from abc import ABC, abstractmethod

class IModel(ABC):
    @abstractmethod
    def find_by_id(self, user_id):
        pass

    @abstractmethod
    def create(self, email, password):
        pass
