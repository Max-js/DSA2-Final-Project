
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
            package.deliveryDeadline = row[5]
            package.weight = row[6]
            hashTable.insert(package.id, package)
    return hashTable

table = ChainingHashTable()
table = loadPackageData("DSA2-Final-Project\CSVFiles\packageCSV.csv", table)

truck1 = Truck(1, addresses[0][2], datetime.timedelta(hours=8), datetime.timedelta(hours=8), 0.0, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck(2, addresses[0][2], datetime.timedelta(hours=9, minutes=5), datetime.timedelta(hours=9, minutes=5), 0.0, 18, [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
truck3 = Truck(3, addresses[0][2], datetime.timedelta(hours=10, minutes=20), datetime.timedelta(hours=10, minutes=20), 0.0, 18, [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33])

def getAddress(address):
    return next((int(row[0]) for row in addresses if address in row[2]), None)

def getDistance(x, y):
    return float(distances[x][y] if distances[x][y] != "" else distances[y][x])

def returnToHub(truck):
    hubDistance = getDistance(getAddress(truck.currentLocation), getAddress(addresses[0][2]))
    truck.currentTime += datetime.timedelta(hours=hubDistance / 18)
    truck.mileage += hubDistance
    truck.currentLocation = addresses[0][2]
    print(f"TRUCK FINAL: ID: {truck.id},  mileage ({truck.mileage}), depart: ({truck.departureTime}), time ({truck.currentTime}), location ({truck.currentLocation})")

def deliverPackages(truck):
    while truck.packages:
        nextAddress = float('inf')
        nextPackage = None

        for packageID in truck.packages:
            package = table.search(packageID)
            package.status = f"Out for delivery on Truck {truck.id}"
            package.leftHub = truck.departureTime
            
            if packageID == 9:
                package.address = "410 S State St"
                package.zip = "84111"

            distance = getDistance(getAddress(truck.currentLocation), getAddress(package.address))
            if distance < nextAddress:
                nextAddress = distance
                nextPackage = package

        if nextPackage:
            if truck.currentLocation == nextPackage.address:
                nextPackage.address = truck.currentLocation
            else:
                truck.mileage += nextAddress
                truck.currentLocation = nextPackage.address
                truck.currentTime += datetime.timedelta(hours=nextAddress / 18)

            nextPackage.deliveryTime = truck.currentTime
            nextPackage.status = "Delivered"
            truck.packages.remove(nextPackage.id)

    returnToHub(truck)

deliverPackages(truck1)
deliverPackages(truck2)
deliverPackages(truck3)

class Main:
    acceptedInputs = [1,2,3,9]
    try:
        print("\nWelcome to the package delivery management system!")
        print(f"Total truck mileage for current route: {truck1.mileage + truck2.mileage + truck3.mileage}")
        print("\nSelect an option or input 9 to exit:")
        userInput = input("""
            1: Search for a specific package by ID
            2: Display all package results
            3: Search for all package statuses within a specific time range
            9: Exit
            """) 
        
        if int(userInput) not in acceptedInputs:
            raise ValueError("Input must be one of the choices: 1, 2, 3, or 9. Please try again.")
        
        if int(userInput) == 9:
            exit()
        
        if int(userInput) == 1:
            specificId = int(input("Please enter the package ID: "))
            specificPackage = table.search(specificId)
            print(specificPackage)

        if int(userInput) == 2:
            for i in range(1,41):
                package = table.search(i)
                print(package)

        if int(userInput) == 3:
            (h, m) = input("Please enter a start time in the format HH:MM: ").split(sep=":")
            startTime = datetime.timedelta(hours=int(h), minutes=int(m))
            (h, m) = input("Please enter an end time in the format HH:MM ").split(sep=":")
            endTime = datetime.timedelta(hours=int(h), minutes=int(m))

            for i in range(1,41):
                package = table.search(i)
                status = package.checkStatus(startTime, endTime)
                print(f"\nPackage ID: {package.id}")
                print(f"Package Status: {status}")

                if status == "At Hub":
                    print(f"Package Scheduled to Leave Hub: {package.leftHub}")
                    print(f"Package Expected Delivery Time: {package.deliveryTime}")

                if status == "En Route":
                    print(f"Package Left Hub: {package.leftHub}")
                    print(f"Package Expected Delivery Time: {package.deliveryTime}")

                if status == "Delivered":
                    print(f"Package Left Hub: {package.leftHub}")
                    print(f"Package Delivery Time: {package.deliveryTime}")

    except ValueError as e:
        print(e) 
