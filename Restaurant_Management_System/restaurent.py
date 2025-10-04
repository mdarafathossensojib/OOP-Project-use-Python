from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")
    
    def view_employee(self):
        if not self.employees:
            print("No employees to display.")
            return
        
        print("Employee List: ")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}, Address: {emp.address}")
