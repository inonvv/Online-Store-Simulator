# This is a sample Python script.
from Classes.Product import Product
from Classes.ShoppingCart import ShoppingCart
from Classes.Store import Store


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # my_store = Store()
    apple = Product("apple", "apple_code", 3, "Fruits & Vegetables")
    orange = Product("orange", "orange_code", 5, "Fruits & Vegetables")
    #
    # my_store.store_inventory.add_product(apple, 5)
    # my_store.store_inventory.add_product(orange, 6)


    shopping_cart = ShoppingCart()
    shopping_cart.add_product(apple, 5)
    shopping_cart.add_product(orange, 10)
    total_price = shopping_cart.calculate_products_price()
    print(total_price)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
