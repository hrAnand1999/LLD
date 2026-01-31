from abc import ABC, abstractmethod
from InventoryManagement.menuItemInterface import MenuItemInterface
from InventoryManagement.menuInterface import MenuIterface

class RestaurantInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def getMenu(self):
        pass

    @abstractmethod
    def addItemToMenu(self, menuItem: MenuItemInterface):
        pass

    @abstractmethod
    def removeItemFromMenu(self, menuItem: MenuItemInterface):
        pass

    @abstractmethod
    def getRating(self):
        pass

    @abstractmethod
    def getAddress(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def addMenu(self, menu: MenuIterface):
        pass