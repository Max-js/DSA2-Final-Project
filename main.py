
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
            package.state = row[3]
            package.zip = row[4]
            package.deliveryTime = row[5]
            package.weight = row[6]
            package.rules = row[7]
            hashTable.insert(package.id, package)
    return hashTable

table = ChainingHashTable()
table = loadPackageData("DSA2-Final-Project\CSVFiles\packageCSV.csv", table)
#table.printHashTable()
#print(ChainingHashTable.search(table, 4))
