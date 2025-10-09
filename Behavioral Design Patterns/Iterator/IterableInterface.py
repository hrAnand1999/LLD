from abc import ABC, abstractmethod

class IterableInterface(ABC):
    @abstractmethod
    def get_iterator(self):
        pass