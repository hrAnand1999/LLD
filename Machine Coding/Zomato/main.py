from InventoryManagement.restaurant import Restaurant
from Address.address import Address
from InventoryManagement.rating import Rating
from InventoryManagement.menu import Menu
from InventoryManagement.menuItem import MenuItem
from InventoryManagement.item import Item
def main():
    address = Address("12345")
    pizzaRating = Rating(4.5)
    burgerRating = Rating(3.0)
    restaurant1Rating = Rating(4.0)
    restaurant1 = Restaurant(address, restaurant1Rating, None, 1, "Good Eats")
    items = [Item("Pizza", "veg"), Item("Burger", "non-veg")]
    menu_items = [MenuItem(restaurant1.getId(), restaurant1.getName(), items[0], pizzaRating, 9.99, 5),
                   MenuItem(restaurant1.getId(), restaurant1.getName(), items[1], burgerRating, 5.99, 3)]
    menu = Menu(menu_items)
    restaurant1.addMenu(menu)

    

    print(f"Restaurant Name: {restaurant1.getName()}")
    print(f"Restaurant Address Pincode: {restaurant1.getAddress()}")
    print(f"Restaurant Rating: {restaurant1.getRating()}")

    print("Menu Items:")
    restaurant1.getMenu()
    
    pastaItem = Item("Pasta", "veg")
    pastaRating = Rating(4.2)
    pastaMenuItem = MenuItem(restaurant1.getId(), restaurant1.getName(), pastaItem, pastaRating, 12.99, 5)
    restaurant1.addItemToMenu(pastaMenuItem)
    print("Menu Items after adding Pasta:")
    restaurant1.getMenu()
    
    restaurant1.removeItemFromMenu(pastaMenuItem)
    print("Menu Items after removing Pasta:")
    restaurant1.getMenu()

if __name__ == "__main__":
    main()