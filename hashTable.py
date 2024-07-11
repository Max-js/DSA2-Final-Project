# HashTable class using chaining.
class ChainingHashTable(object):
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      

    def insert(self, packageId, package):
        key = hash(packageId) % len(self.table)
        if [packageId, package] not in self.table[key]:
           self.table[key].append([packageId, package])
        return
 
    def search(self, packageId):
        # get the package list where this key would be.
        location = hash(packageId) % len(self.table)
        packageList = self.table[location]
 
        # search for the package ID in the package list
        for package in packageList:
          if package[0] == packageId:
            return package[1]
        return None
 
    def remove(self, packageId):
        # get the package list where this item will be removed from.
        location = hash(packageId) % len(self.table)
        packageList = self.table[location]
 
        # remove the item from the bucket list if it is present.
        for package in packageList:
          if package[0] == packageId:
              packageList.remove([package[0], package[1]])

    
    def printHashTable(self):
       print(self.table)
       return