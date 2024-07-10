class Truck(object):
    def __init__(self, truckId, currentLocation):
        self.id = truckId
        self.location = currentLocation


    def __str__(self):
        return (self.id, self.currentLocation)