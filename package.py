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
        return f"\n Address: {self.address},\n City: {self.city},\n Zip Code: {self.zip},\n Left Hub: {self.leftHub},\n Delivery Time: {self.deliveryTime},\n Delivery Deadline: {self.deliveryDeadline},\n Weight: {self.weight},\n Status: {self.status} \n"
    
    def __repr__(self):
        return self.__str__()
