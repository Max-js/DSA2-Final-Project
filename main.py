
import csv
import datetime
from truck import Truck
from package import *
from hashTable import *

#Necessary??
with open("DSA2-Final-Project\CSVFiles\distanceCSV.csv") as distanceCSV:
    distances = list(csv.reader(distanceCSV))
    
""" with open("DSA2-Final-Project\CSVFiles\packageCSV.csv") as packageCSV:
    packages = list(csv.reader(packageCSV)) """

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

truck1 = Truck("4001 South 700 East", datetime.time(hour=10), 0.0, 16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck("4001 South 700 East", datetime.time(hour=10), 0.0, 16, 18, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
truck3 = Truck("4001 South 700 East", datetime.time(hour=10), 0.0, 16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33])


def getAddress(addressCSV, address):
    with open(addressCSV) as addressData:
        for row in csv.reader(addressData):
            if address in row[2]:
                return int(row[0])


