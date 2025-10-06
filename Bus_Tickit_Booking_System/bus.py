class Bus:
    def __init__(self, bus_number, name, route, total_seats):
        self.bus_number = bus_number
        self.name = name
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False

