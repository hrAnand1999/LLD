from abc import ABC, abstractmethod


class ObserverInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def update(self, message):
        pass