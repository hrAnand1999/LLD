from InventoryManagement.restaurantInterface import RestaurantInterface
from Address.address import AddressInterface
from InventoryManagement.ratingInterface import RatingInterface
from InventoryManagement.menuInterface import MenuIterface
from InventoryManagement.menuItemInterface import MenuItemInterface

class Restaurant(RestaurantInterface):

    def __init__(self, address: AddressInterface, rating: RatingInterface, menu: MenuIterface,
                 id: int, name: str):
        self.address = address
        self.rating = rating
        self.menu = menu
        self.id = id
        self.name = name

    def getMenu(self):
        if self.menu is None:
            return []
        return self.menu.getItemLists()
    
    def addItemToMenu(self, menuItem: MenuItemInterface):
        self.menu.addItemToMenu(menuItem)

    def removeItemFromMenu(self, menuItem: MenuItemInterface):
        self.menu.removeItemFromMenu(menuItem)
    
    def getRating(self):
        return self.rating.getRating()  
    
    def getAddress(self):
        return self.address.getPincode()
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def addMenu(self, menu: MenuIterface):
        self.menu = menu
        print("Menu added to restaurant")
    
