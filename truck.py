class Truck(object):
    def __init__(self, id = None, currentLocation = None, currentTime = None, departureTime = None, mileage = 0.0, speed = None, packages = None):
        self.id = id
        self.location = currentLocation
        self.currentTime = currentTime
        self.departureTime = departureTime
        self.mileage = mileage
        self.speed = speed
        self.packages = packages

    def __str__(self):
        return f"\n Truck ID: {self.id},\n Current Location: {self.location},\n Current Time: {self.currentTime},\n Departure Time: {self.departureTime},\n Mileage: {self.mileage},\n Speed: {self.speed},\n Packages: {self.packages} \n"
    
    def __repr__(self):
        return self.__str__()
