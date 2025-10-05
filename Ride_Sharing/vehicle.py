from abc import ABC

class Vehicle(ABC):
    speed = {
        'car' : 60,
        'bike' : 50,
        'cng' : 30
    }

    def __init__(self, vehicle_type, license_plate, rate_per_km):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate_per_km = rate_per_km
    
class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate_per_km):
        super().__init__(vehicle_type, license_plate, rate_per_km)

class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate_per_km):
        super().__init__(vehicle_type, license_plate, rate_per_km)

class Cng(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate_per_km):
        super().__init__(vehicle_type, license_plate, rate_per_km)