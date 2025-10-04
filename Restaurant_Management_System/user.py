from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)

    def view_employee(self, restaurent):
        restaurent.view_employee()

    def add_new_item(self, restaurent, item):
        restaurent.menu.add_item(item)
    
    def remove_item(self, restaurent, item_name):
        restaurent.menu.remove_item(item_name)

    def view_item(self, restaurent):
        restaurent.menu.show_menu()

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Customar(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
    
    def view_menu(self, restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print(f'Only {item.quantity} items available in stock.')
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print(f'Item added to cart Successfully: {item.name}')
        else:
            print(f'Item Not Found: {item_name}')

    def view_cart(self):
        if not self.cart.items:
            print("Cart is Empty.")
        else:
            print("*****Cart*****")
            print("Name\tPrice\tQuantity")
            for item, quantity in self.cart.items.items():
                print(f"{item.name}\t{item.price}\t{quantity}")
            print(f'Total Price: {self.cart.total_price}')

    def pay_bill(self):
        print(f"Total {self.cart.total_price} Tk Paid Successfully.")
        self.cart.clear_cart()
