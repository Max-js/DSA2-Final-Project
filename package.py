import datetime
class Package(object):
    def __init__(self, id = None, address = None, city = None, zipCode = None, leftHub = None, deliveryTime = None, deliveryDeadline = None, weight = None, status = 'Hub'):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zipCode
        self.leftHub = leftHub
        self.deliveryTime = deliveryTime
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"\n ID: {self.id}, \n Address: {self.address},\n City: {self.city},\n Zip Code: {self.zip},\n Left Hub: {self.leftHub},\n Delivery Deadline: {self.deliveryDeadline},\n Status: {self.status},\n Delivery Time: {self.deliveryTime},\n Weight: {self.weight} \n"
    
    def __repr__(self):
        return self.__str__()
    
    #FIX extra condition:
    def checkStatus(self, startTime, endTime):
        if self.deliveryTime < startTime or startTime <= self.deliveryTime <= endTime:
            return "Delivered"
        elif startTime <= self.leftHub and self.deliveryTime < endTime:
            return "Delivered"
        elif startTime <= self.leftHub <= endTime:
            return "En Route"
        elif startTime < self.leftHub and not (self.deliveryTime <= endTime):
            return "At Hub"
        else:
            return "En Route"
