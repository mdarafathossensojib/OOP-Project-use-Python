from food_item import FoodItem
from menu import Menu
from orders import Order
from user import Admin, Customar, Employee
from restaurent import Restaurent

mamar_restaurent = Restaurent("Mamar Restaurent")

def customar_actions():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    custormar = Customar(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome {custormar.name} to {mamar_restaurent.name}")
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            custormar.view_menu(mamar_restaurent)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            quantity = int(input("Enter Quantity: "))
            custormar.add_to_cart(mamar_restaurent, item_name, quantity)
        elif choice == 3:
            custormar.view_cart()
        elif choice == 4:
            custormar.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid Choice!")
    
def admin_actions():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone = input("Enter Your Phone: ")
    address = input("Enter Your Address: ")

    admin = Admin(name=name, phone=phone, email=email, address=address)

    while True:
        print(f"Welcome {admin.name} to {mamar_restaurent.name}")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Add New Item")
        print("4. View Item")
        print("5. Remove Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            emp_name = input("Enter Employee Name: ")
            emp_email = input("Enter Employee Email: ")
            emp_phone = input("Enter Employee Phone: ")
            emp_address = input("Enter Employee Address: ")
            emp_age = int(input("Enter Employee Age: "))
            emp_designation = input("Enter Employee Designation: ")
            emp_salary = int(input("Enter Employee Salary: "))

            employee = Employee(name=emp_name, phone=emp_phone, email=emp_email, address=emp_address, age=emp_age, designation=emp_designation, salary=emp_salary)
            admin.add_employee(mamar_restaurent, employee)
        elif choice == 2:
            admin.view_employee(mamar_restaurent)
        elif choice == 3:
            item_name = input("Enter Item Name: ")
            item_price = float(input("Enter Item Price: "))
            item_quantity = int(input("Enter Item Quantity: "))

            item = FoodItem(name=item_name, price=item_price, quantity=item_quantity)
            admin.add_new_item(mamar_restaurent, item)
        elif choice == 4:
            admin.view_item(mamar_restaurent)
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.remove_item(mamar_restaurent, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid Choice!")


while True:
    print("Welcome to Restaurent Management System\n1. Admin\n2. Customar\n3. Exit")
    user_type = int(input("Enter Your Choice: "))

    if user_type == 1:
        admin_actions()
    elif user_type == 2:
        customar_actions()
    elif user_type == 3:
        print("Thank You for using Restaurent Management System")
        break
    else:
        print("Invalid Choice! Please try again to select valid Option.")