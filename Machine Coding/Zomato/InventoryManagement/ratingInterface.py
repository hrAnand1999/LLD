from abc import ABC, abstractmethod
# from InventoryManagement.menuItemInterface import MenuItemInterface

class RatingInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getRating(self):
        pass

    # @abstractmethod
    # def getAddress(self):
    #     pass

    # @abstractmethod
    # def getName(self):
    #     pass

    # @abstractmethod
    # def getMenu(self):
    #     pass

    # @abstractmethod
    # def addItemToMenu(self, menuItem: MenuItemInterface):
    #     pass

    # @abstractmethod
    # def removeItemFromMenu(self, menuItem: MenuItemInterface):
    #     pass