#Maxwell Smith
#WGU Student ID: 011585360
#DSA2 Final Project

import csv
import datetime
from truck import Truck
from package import *
from hashTable import *

#Initialize necessary CSV files for use throughout the program
with open("DSA2-Final-Project\CSVFiles\distanceCSV.csv") as distanceCSV:
    distances = list(csv.reader(distanceCSV))

with open("DSA2-Final-Project\CSVFiles\/addressCSV.csv") as addressCSV:
    addresses = list(csv.reader(addressCSV))
    
with open("DSA2-Final-Project\CSVFiles\packageCSV.csv") as packageCSV:
    packages = list(csv.reader(packageCSV))

#Load package data into Hashtable while assigning values from package CSV
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
            package.status = "Hub"
            hashTable.insert(package.id, package)
    return hashTable

#Initialize Hash Table and load data into it
table = ChainingHashTable()
table = loadPackageData("DSA2-Final-Project\CSVFiles\packageCSV.csv", table)

#Initialize and manually load trucks
truck1 = Truck(1, addresses[0][2], datetime.timedelta(hours=8), datetime.timedelta(hours=8), 0.0, 18, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40])
truck2 = Truck(2, addresses[0][2], datetime.timedelta(hours=9, minutes=5), datetime.timedelta(hours=9, minutes=5), 0.0, 18, [3, 6, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
truck3 = Truck(3, addresses[0][2], datetime.timedelta(hours=10, minutes=20), datetime.timedelta(hours=10, minutes=20), 0.0, 18, [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33])

#Return the address number from address string
def getAddress(address):
    return next((int(row[0]) for row in addresses if address in row[2]), None)

#Return the distance between two addresses
def getDistance(x, y):
    return float(distances[x][y] if distances[x][y] != "" else distances[y][x])

#Returns truck to hub, setting address, time, and accounting for final trip mileage
def returnToHub(truck):
    hubDistance = getDistance(getAddress(truck.currentLocation), getAddress(addresses[0][2]))
    truck.currentTime += datetime.timedelta(hours=hubDistance / 18)
    truck.mileage += hubDistance
    truck.currentLocation = addresses[0][2]

#Execute the delivery of packages based on truck
def deliverPackages(truck):
    while truck.packages:
        nextAddress = float('inf')
        nextPackage = None

        #Iterate through packages on truck
        for packageID in truck.packages:
            package = table.search(packageID)
            package.status = "En Route"
            package.leftHub = truck.departureTime
            
            #Manually change package #9 address when new address is available
            if packageID == 9:
                package.address = "410 S State St"
                package.zip = "84111"

            #Use nearest neighbor algorithm to determine next package that should be delivered from packages remaining on truck
            distance = getDistance(getAddress(truck.currentLocation), getAddress(package.address))
            if distance < nextAddress:
                nextAddress = distance
                nextPackage = package

        #If there is a next packge, then deliver it
        if nextPackage:
            #If packages are being delivered to the same location, do not add mileage or time
            if truck.currentLocation == nextPackage.address:
                nextPackage.address = truck.currentLocation
            else:
                truck.mileage += nextAddress
                truck.currentLocation = nextPackage.address
                truck.currentTime += datetime.timedelta(hours=nextAddress / 18)

            nextPackage.deliveryTime = truck.currentTime
            nextPackage.status = "Delivered"
            truck.packages.remove(nextPackage.id)

    #Return truck to hub from current location once all packages have been delivered
    returnToHub(truck)

#Execute delivery of packages for each truck
deliverPackages(truck1)
deliverPackages(truck2)
deliverPackages(truck3)

#Handles UI elements
class Main:
    #List of acceptable inputs for comparison
    acceptedInputs = [1,2,3,9]
    try:
        print("\nWelcome to the WGUPS package delivery management system!")
        print(f"Total truck mileage for current route: {truck1.mileage + truck2.mileage + truck3.mileage}")
        print("\nSelect an option or input 9 to exit:")
        userInput = input("""
            1: Search for a specific package by ID
            2: Display all package results
            3: Search for all package statuses within a specific time range
            9: Exit
            """) 
        
        #Raise error if user inputs anything other than one of the 4 accepted inputs.
        if int(userInput) not in acceptedInputs:
            raise ValueError("Input must be one of the choices: 1, 2, 3, or 9. Please try again.")
        
        #Handle Exit
        if int(userInput) == 9:
            exit()
        
        #Handle search for specific package ID
        if int(userInput) == 1:
            specificId = int(input("Please enter the package ID: "))
            specificPackage = table.search(specificId)
            print(specificPackage)

        #Handle option to display all package results
        if int(userInput) == 2:
            for i in range(1,41):
                package = table.search(i)
                print(package)

        #Handle package status search within specific time frame
        if int(userInput) == 3:
            #Take user time input and convert to time delta for comparison
            (h, m) = input("Please enter a start time in the format HH:MM: ").split(sep=":")
            startTime = datetime.timedelta(hours=int(h), minutes=int(m))
            (h, m) = input("Please enter an end time in the format HH:MM ").split(sep=":")
            endTime = datetime.timedelta(hours=int(h), minutes=int(m))

            #Iterate through all packages
            for i in range(1,41):
                package = table.search(i)

                #Return status of each package within requested time frame
                status = package.checkStatus(startTime, endTime)
                print(f"\nPackage ID: {package.id}")
                print(f"Package Status: {status}")

                #Adjust output to be more appropriate based on package status
                if status == "At Hub":
                    print(f"Package Scheduled to Leave Hub: {package.leftHub}")
                    print(f"Package Expected Delivery Time: {package.deliveryTime}")

                if status == "En Route":
                    print(f"Package Left Hub: {package.leftHub}")
                    print(f"Package Expected Delivery Time: {package.deliveryTime}")

                if status == "Delivered":
                    print(f"Package Left Hub: {package.leftHub}")
                    print(f"Package Delivery Time: {package.deliveryTime}")

    #Handle erroneous input
    except ValueError as e:
        print(e) 
