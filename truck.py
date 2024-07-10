class Truck(object):
    def __init__(self, currentLocation = None, packages = None, currentTime = None):
        self.location = currentLocation
        self.packages = packages
        self.currentTime = currentTime


def printTruckDetails(self):
    print("Location: " + self.location)
    print("Packages: " + self.packages)
    print("Current Time: " + self.currentTime)