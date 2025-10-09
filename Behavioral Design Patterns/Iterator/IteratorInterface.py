from abc import ABC, abstractmethod

class IteratorInterface(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass