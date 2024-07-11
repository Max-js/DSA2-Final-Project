class Package(object):
    def __init__(self, id = None, address = None, city = None, state = None, zipCode = None, deliveryTime = None, weight = None, rules = None, status = 'Hub'):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipCode
        self.deliveryTime = deliveryTime
        self.weight = weight
        self.rules = rules
        self.status = status

    def __str__(self):
        return f"Address: {self.address}, City: {self.city}, State: {self.state}, Zip Code: {self.zip}, Delivery Time: {self.deliveryTime}, Weight: {self.weight}, Rules: {self.rules}, Status: {self.status}"
    
    def __repr__(self):
        return self.__str__()
    
#Probably not needed
def printPackageDetails(self):
    print("Package ID: ", self.id)
    print("Package Address: ", self.address)
    print("Package City: ", self.city)
    print("Package State: ", self.state)
    print("Package Zip Code: ", self.zip)
    print("Package Delivery Time: ", self.deliveryTime)
    print("Package Weight: ", self.weight)
    print("Package Rules: ", self.rules)
    print("Package Status: ", self.status)
    return

