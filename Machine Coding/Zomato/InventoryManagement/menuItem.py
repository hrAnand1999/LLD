from InventoryManagement.menuItemInterface import MenuItemInterface
from InventoryManagement.itemInterface import ItemInterface
from InventoryManagement.ratingInterface import RatingInterface


class MenuItem(MenuItemInterface):

    def __init__(self, restaurantId: int, restaurantName: str, item: ItemInterface,
                  rating: RatingInterface, price: int, quantity: int):
        self.rating = rating
        self.item = item
        self.price = price
        self.quantity = quantity
        self.restaurantId = restaurantId
        self.restaurantName = restaurantName

    def isAvailable(self):
        return self.quantity > 0
    
    def getQuantity(self):
        return self.quantity
    
    def getRating(self):
        return self.rating.getRating()
    
    def reserve(self, amount):
        if amount > self.quantity:
            print("Not available selected quantity")
            return
        self.quantity = self.quantity - amount
        print("Reserved")

    def release(self, amount):
        self.quantity = self.quantity + amount
        print("Released")

    def getName(self):
        return self.item.getName()
    
    def getMenuItem(self):
        return self
    
    def getPrice(self):
        return self.price

        