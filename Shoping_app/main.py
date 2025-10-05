from item import Product
from shop import Shop
from user import Seller, Customer

shop = Shop("My Online Shop")

def customer_actions(username, email, password):
    customar = Customer(username=username, email=email, password=password)
    while True:
        print(f"Welcome {customar.username} to {shop.name}")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customar.view_products(shop)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            customar.add_to_cart(shop, item_name, quantity)
        elif choice == 3:
            customar.view_cart()
        elif choice == 4:
            item_name = input("Enter Item Name to Remove from Cart: ")
            customar.remove_from_cart(item_name)
        elif choice == 5:
            customar.checkout()
        elif choice == 6:
            break
        else:
            print("Invalid Choice!")

def seller_actions(username, email, password):
    seller = Seller(username=username, email=email, password=password)
    while True:
        print(f"Welcome {seller.username} to {shop.name}")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Show Products")
        print("4. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            item_name = input("Enter Product Name: ")
            item_price = float(input("Enter Product Price: "))
            item_stock = int(input("Enter Product Stock: "))
            product = Product(name=item_name, price=item_price, stock=item_stock)
            seller.add_product(shop, product)
        elif choice == 2:
            item_name = input("Enter Product Name to Remove: ")
            product = shop.find_product(item_name)
            if product:
                seller.remove_product(shop, product)
            else:
                print(f'Product not found: {item_name}')
        elif choice == 3:
            seller.show_products(shop)
        elif choice == 4:
            break
        else:
            print("Invalid Choice!")

data = {} # {username: password}
def customar():
    while True:
        print("1. Login\n2. Register\n3. Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if username in data and data[username][1] == password:
                print("Login Successful!")
                customer_actions(username, data[username][0], password)
            else:
                print("Invalid Credentials! Please try again.")
        elif choice == 2:
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            d = [email, password]
            data[username] = d
            print("Registration Successful! Please login to continue.")    
        elif choice == 3:
            break
        else:
            print("Invalid Choice!")       

def seller():
    while True:
        print("1. Login\n2. Register\n3. Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if username in data and data[username][1] == password:
                print("Login Successful!")
                seller_actions(username, data[username][0], password)
            else:
                print("Invalid Credentials! Please try again.")
        elif choice == 2:
            username = input("Enter Username: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            d = [email, password]
            data[username] = d
            print("Registration Successful! Please login to continue.")    
        elif choice == 3:
            break
        else:
            print("Invalid Choice!")

while True:
    print("Welcome to the Shopping App")
    print("1. Customer")
    print("2. Seller")
    print("3. Exit")

    user_type = int(input("Enter Your Choice: "))

    if user_type == 1:
        customar()
    elif user_type == 2:
        seller()
    elif user_type == 3:
        print("Thank you for using the Shopping App!")
        break
    else:
        print("Invalid Choice!")