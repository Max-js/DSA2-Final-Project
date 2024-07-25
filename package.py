class Package(object):
    #Define Package base class and necessary parameters
    def __init__(self, id = None, address = None, city = None, zipCode = None, leftHub = None, truck = None, deliveryTime = None, deliveryDeadline = None, weight = None, status = 'Hub'):
        self.id = id
        self.address = address
        self.city = city
        self.zip = zipCode
        self.leftHub = leftHub
        self.deliveryTime = deliveryTime
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        self.status = status

    #Define "pretty" printable format for package class
    def __str__(self):
        return f"\n ID: {self.id}, \n Address: {self.address},\n City: {self.city},\n Zip Code: {self.zip},\n Left Hub: {self.leftHub},\n Truck: {self.truck.id},\n Delivery Deadline: {self.deliveryDeadline},\n Status: {self.status},\n Delivery Time: {self.deliveryTime},\n Weight: {self.weight} \n"
    
    #Enables package class printable representation to be consistent when accessing a package object
    def __repr__(self):
        return self.__str__()
    
    #Returns package status based on a given time frame
    def checkStatus(self, startTime, endTime):
        if self.deliveryTime < startTime or startTime <= self.deliveryTime <= endTime:
            return "Delivered"
        
        if self.leftHub < endTime < self.deliveryTime:
            return "En Route"

        if endTime < self.leftHub:
            return "At Hub"
