from abc import ABC, abstractmethod

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
    
    def request_ride(self, ride_sharing, destination):
        pass

    def show_curr_ride(self):
        if self.curr_Ride:
            print(f"Current Ride from {self.curr_Ride.start_location} to {self.curr_Ride.end_location}")
        else:
            print("No current ride.")
    
    def pay_ride(self, amount):
        if self.wallet >= amount:
            self.wallet -= amount
            print(f"Ride paid. Remaining Balance: {self.wallet}")
        else:
            print("Insufficient balance to pay for the ride.")
    
class Driver(User):
    def __init__(self, name, email, nid, curr_location):
        super().__init__(name, email, nid)
        self.curr_location = curr_location
        self.wallet = 0
    
    def diplay_profile(self):
        print(f"Driver Name: {self.name} ans Email: {self.email}")
    
    def accpet_ride(self, ride):
        pass
