class Package:
    def __init__(self, packageId, address, city, state, zipCode, deliveryTime, date, status):
        self.id = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipCode
        self.deliveryTime = deliveryTime
        self.date = date
        self.status = status

    
    def __str__(self):
        return (self.id, self.address, self.city, self.state, self.zip, self.deliveryTime, self.date, self.status)
