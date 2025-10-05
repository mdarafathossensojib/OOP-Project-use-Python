from abc import ABC
from order import Order

class User(ABC):
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Seller(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
    
    def add_product(self, shope, item):
        shope.add_product(item)
    
    def remove_product(self, shope, item):
        shope.remove_product(item)
    
    def show_products(self, shope):
        shope.show_products()

class Customer(User):
    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.cart = Order()
    
    def view_products(self, shope):
        shope.show_products()
    
    def add_to_cart(self, shope, item_name, quantity):
        item = shope.find_product(item_name)
        if item:
            if quantity <= item.stock:
                item.stock = quantity
                self.cart.add_item(item)
                print(f'Item added to cart Successfully: {item.name}')
            else:
                print(f'Only {item.stock} items available in stock.')
        else:
            print(f'Item Not Found: {item_name}')

    def remove_from_cart(self, item_name):
        self.cart.remove_item(item_name)
    
    def view_cart(self):
        if not self.cart.items:
            print("Cart is Empty.")
        else:
            print("Items in Cart:\nName\tPrice\tQuantity")
            for item, quantity in self.cart.items.items():
                print(f"{item.name}\t{item.price}\t{quantity}")
            print(f"Total Price: {self.cart.total_price}")
    
    def checkout(self):
        if not self.cart.items:
            print("Cart is Empty. Cannot proceed to checkout.")
        else:
            print("Checkout Successful!")
            print(f"Total Amount Paid: {self.cart.total_price}")
            self.cart.clear_cart()
    
