from abc import ABC, abstractmethod


class MenuItemInterface(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def isAvailable(self):
        pass

    @abstractmethod
    def getRating(self):
        pass

    @abstractmethod
    def getQuantity(self):
        pass

    @abstractmethod
    def reserve(self, amount: int):
        pass

    @abstractmethod
    def release(self, amount: int):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass

