from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching, RideSharing

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    
    @abstractmethod
    def diplay_profile(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rider(User):
    def __init__(self, name, email, nid, curr_location, initial_balance):
        super().__init__(name, email, nid)
        self.curr_location = curr_location
        self.wallet = initial_balance
        self.curr_Ride = None

    def diplay_profile(self):
        print(f"Rider Name: {self.name} ans Email: {self.email}")

    def load_cash(self, amount):
        self.wallet += amount
        print(f"New Balance: {self.wallet}")
    
    def update_location(self, new_location):
        self.curr_location = new_location
        print(f"New Location: {self.curr_location}")
    
    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        ride.rider = self
        self.curr_Ride = ride
        print("YAY!! We got a ride for You.")

    def show_curr_ride(self):
        print("Ride Details: ")
        print(f"Rider : {self.name}\nDriver : {self.curr_Ride.driver.name}")
        print(f"Selected Vehicle : {self.curr_Ride.vehicle.vehicle_type}")
        print(f"From : {self.curr_Ride.start_location} To : {self.curr_Ride.end_location}")
        print(f"Fare : {self.curr_Ride.fare}")

class Driver(User):
    def __init__(self, name, email, nid, curr_location):
        super().__init__(name, email, nid)
        self.curr_location = curr_location
        self.wallet = 0
    
    def diplay_profile(self):
        print(f"Driver Name: {self.name} ans Email: {self.email}")
    
    def accpet_ride(self, ride):
        ride.start_ride()
        ride.set_driver(self)
    
    def reach_destination(self, ride):
        ride.end_ride()
        print("You have reached your destination.")

