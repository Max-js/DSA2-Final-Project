class Truck(object):
    #Define Truck base class and necessary parameters
    def __init__(self, id = None, currentLocation = None, currentTime = None, departureTime = None, mileage = 0.0, speed = None, packages = None):
        self.id = id
        self.currentLocation = currentLocation
        self.currentTime = currentTime
        self.departureTime = departureTime
        self.mileage = mileage
        self.speed = speed
        self.packages = packages

    #Define "pretty" printable format for truck class
    def __str__(self):
        return f"\n Truck ID: {self.id},\n Current Location: {self.currentLocation},\n Current Time: {self.currentTime},\n Departure Time: {self.departureTime},\n Mileage: {self.mileage},\n Speed: {self.speed},\n Packages: {self.packages} \n"
    
    #Enables truck class printable representation to be consistent when accessing a truck object
    def __repr__(self):
        return self.__str__()
