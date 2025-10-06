from passenger import Passenger
from bus import Bus

class BusSystem:
    def __init__(self, name):
        self.name = name
        self.buses = []
        self.passengers = []

    def book_ticket(self, bus_number, name, phone):
        for bus in self.buses:
            if bus.bus_number == bus_number:
                if bus.book_seat():
                    new_passenger = Passenger(name, phone, bus)
                    self.passengers.append(new_passenger)
                    print("Tickit book Successfully!")
                    print(f"Bus Name: {bus.name} and Seat Number is {bus.booked_seats}")

                else:
                    print("No Seat Available!")
                return
        print("Bus Not Found")
        
    
    def add_bus(self, bus_number, name, route, total_seats):
        bus = Bus(bus_number, name, route, total_seats)
        self.buses.append(bus)
    
    def view_buses(self):
        if len(self.buses) > 0:
            for bus in self.buses:
                print(f"Bus Number: {bus.bus_number}, Name: {bus.name}, Route: {bus.route}, Available Seats: {bus.available_seats()}")
            return True
        else:
            print("No Bus Available!")
            return False
    
    
    def view_seats(self, bus_number):
        for bus in self.buses:
            if bus.bus_number == bus_number:
                if bus.available_seats() > 0:
                    seat = bus.total_seats - bus.available_seats()
                    for i in range(seat+1, bus.total_seats+1):
                        print(f"Seat Number {i} and Total fare is 500tk.")
                else:
                    print("No Seat Available!")
                return
        print("Bus not Found!")
    
    def view_passenger(self):
        if len(self.passengers) > 0:
            for passenger in self.passengers:
                print(f"Passenger Name: {passenger.name}, Phone: {passenger.phone}, Bus Number: {passenger.bus.bus_number}")
        else:
            print("Currently No Passengers Here!")