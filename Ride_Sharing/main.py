from ride import Ride, RideRequest, RideMatching, RideSharing
from user import Rider, Driver
from vehicle import Car, Bike, Cng

uber = RideSharing("Uber")
arafat = Rider("Arafat", "arafat@gmail.com", "124545", "Dhanmondi", 500)
bappy = Driver("Bappy", "bappy@gmail.com", "4565", "Uttara")
uber.add_rider(arafat)
uber.add_driver(bappy)
print(uber)
