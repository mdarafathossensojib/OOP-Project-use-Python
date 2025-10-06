from bus import Bus
from passenger import Passenger
from admin import Admin
from busSystem import BusSystem

bus_system = BusSystem("Bangladesh Bus Booking System")

def admin_action():
    admin = Admin()
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if not admin.authenticate(username, password):
        print("Authentication failed!")
    else:
        print("Login Successfull!")

        while True:
            print("1. Add Bus")
            print("2. View Buses")
            print("3. View Passengers")
            print("4. Logout")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                bus_number = input("Enter bus number: ")
                name = input("Enter bus name: ")
                route = input("Enter bus route: ")
                total_seats = int(input("Enter total seats: "))
                admin.add_bus(bus_system, bus_number, name, route, total_seats)
                print("Bus added successfully!")
            elif choice == 2:
                admin.view_buses(bus_system)
            elif choice == 3:
                admin.view_passengers(bus_system)
            elif choice == 4:
                break
            else:
                print("Invalid choice!")
        
        
while True:
    print(f"Welcome to {bus_system.name}")
    print("1. Admin Login \n2. Book Tickit \n3. View Buses \n4. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        admin_action()
    elif choice == 2:
        name = input("Enter Your Name: ")
        phone = input("Enter Your Phone Number: ")
        bus_number = input("Enter Journey Bus Number: ")
        bus_system.book_ticket(bus_number, name, phone)
    elif choice == 3:
        flag = bus_system.view_buses()
        if flag:
            print("1. View available seat Number and fare \n2. Exit")
            c = int(input("Enter Your Choice : "))
            if c == 1:
                number = input("Enter Bus Number you want to see: ")
                bus_system.view_seats(number)
            elif c == 2:
                continue
            else:
                print("Invalid Choice!")
        
    elif choice == 4:
        break
    else:
        print("Invalid Choice!")