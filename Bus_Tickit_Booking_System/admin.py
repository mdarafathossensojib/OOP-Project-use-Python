class Admin:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def add_bus(self, bus_system, bus_number, name, route, total_seats):
        bus_system.add_bus(bus_number, name, route, total_seats)
    
    def view_buses(self, bus_system):
        flag = bus_system.view_buses()
    
    def view_passengers(self, bus_system):
        bus_system.view_passenger()
    