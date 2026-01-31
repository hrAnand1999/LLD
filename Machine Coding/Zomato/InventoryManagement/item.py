from InventoryManagement.itemInterface import ItemInterface

class Item(ItemInterface):

    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type