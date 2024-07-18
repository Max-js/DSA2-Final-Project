
import csv
import datetime
from truck import Truck
from package import *
from hashTable import *

with open("DSA2-Final-Project\CSVFiles\distanceCSV.csv") as distanceCSV:
    distances = list(csv.reader(distanceCSV))

with open("DSA2-Final-Project\CSVFiles\/addressCSV.csv") as addressCSV:
    addresses = list(csv.reader(addressCSV))
    
with open("DSA2-Final-Project\CSVFiles\packageCSV.csv") as packageCSV:
    packages = list(csv.reader(packageCSV))

def loadPackageData(packageCSV, hashTable):
    with open(packageCSV) as packageData:
        for row in csv.reader(packageData):
            package = Package()
            package.id = int(str.strip(row[0]))
            package.address = row[1]
            package.city = row[2]
            package.zip = row[4]
            package.deliveryTime = row[5]
            package.weight = row[6]
            hashTable.insert(package.id, package)
    return hashTable

table = ChainingHashTable()
table = loadPackageData("DSA2-Final-Project\CSVFiles\packageCSV.csv", table)
#table.printHashTable()
#print(ChainingHashTable.search(table, 4))

truck1 = Truck(1, addresses[0][2], datetime.timedelta(hours=8), 0.0, 16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck(2, addresses[0][2], datetime.timedelta(hours=9, minutes=5), 0.0, 16, 18, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
truck3 = Truck(3, addresses[0][2], datetime.timedelta(hours=11), 0.0, 16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33])

def getAddress(address):
    return next((int(row[0]) for row in addresses if address in row[2]), None)

def getDistance(x, y):
    return float(distances[x][y] if distances[x][y] != "" else distances[y][x])

def deliverPackages(truck):
    #print(len(truck.packages))
    count = 0
    for packageID in truck.packages:
        package = table.search(packageID)
        package.status = f"Out for delivery on Truck {truck.id}"
        package.leftHub = truck.departureTime

        nextAddress = 1000
        nextPackage = None
        if getDistance(getAddress(truck.location), getAddress(package.address)) <= nextAddress:
            nextAddress = getDistance(getAddress(truck.location), getAddress(package.address))
            nextPackage = package

        truck.mileage += nextAddress
        truck.address = nextPackage.address
        truck.currentTime += datetime.timedelta(hours=nextAddress / 18)
        nextPackage.status = "Delivered"
        truck.departureTime = nextPackage.deliveryTime
        #Necessary?
        count += 1

    #add distance from final location to hub:
    #getDistance(truck.currentLocation, addresses[0][2])
deliverPackages(truck3)
