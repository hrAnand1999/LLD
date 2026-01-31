from abc import ABC, abstractmethod

class MenuIterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def addItemToMenu(self):
        pass

    @abstractmethod
    def removeItemFromMenu(self):
        pass

    @abstractmethod
    def getItemLists(self):
        pass