class Truck(object):
    def __init__(self, currentLocation = None, departureTime = None, mileage = None, speed = None, load = None, packages = None):
        self.location = currentLocation
        self.departureTime = departureTime
        self.mileage = mileage
        self.speed = speed
        self.load = load
        self.packages = packages

    def __str__(self):
        return f"\n Current Location: {self.location},\n Departure Time: {self.departureTime},\n Mileage: {self.mileage},\n Speed: {self.speed},\n Load: {self.load},\n Packages: {self.packages} \n"
    
    def __repr__(self):
        return self.__str__()
