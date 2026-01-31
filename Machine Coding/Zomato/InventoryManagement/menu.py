from InventoryManagement.menuInterface import MenuIterface
from InventoryManagement.menuItemInterface import MenuItemInterface


class Menu(MenuIterface):

    def __init__(self, menuItems: list[MenuItemInterface]):
        self.menuItems = menuItems

    def removeItemFromMenu(self, menuItem: MenuItemInterface):
        if menuItem not in self.menuItems:
            print("Menu Item not present")
            return
        self.menuItems.remove(menuItem)
        print("Menu Item removed")

    def addItemToMenu(self, menuItem: MenuItemInterface):
        if menuItem  in self.menuItems:
            print("Menu Item already present")
            return
        self.menuItems.append(menuItem)
        print("Menu Item added")

    def getItemLists(self):
        for menuItem in self.menuItems:
            print(f'name: {menuItem.getName()}, price: {menuItem.getPrice()}')
