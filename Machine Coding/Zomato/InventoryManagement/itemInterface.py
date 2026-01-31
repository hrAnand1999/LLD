from abc import ABC, abstractmethod

class ItemInterface(ABC):

    def __init__(self):
        super().__init__()

    
    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getType(self):
        pass