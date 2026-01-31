from abc import ABC, abstractmethod

class IObserver(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, msg: str):
        pass