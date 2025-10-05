from datetime import datetime

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def __str__(self):
        return f"Welcome to {self.company_name} with {len(self.riders)} riders and {len(self.drivers)} drivers."

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.fare = None

    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.fare
        self.driver.wallet += self.fare

    def __repr__(self):
        return f"Ride Details. From {self.start_location} to {self.end_location}, Fare: {self.fare}"
    

class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location
        
class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            print("Looking for drivers......")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.curr_location, ride_request.end_location)
            driver.accpet_ride(ride)
            return ride
        else:
            print("No drivers available at the moment.")
            return None
