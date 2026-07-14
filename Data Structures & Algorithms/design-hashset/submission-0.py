class MyHashSet:

    def __init__(self):
        self.set=[]# Initialize an empty list to store the elements of the hash set
        

    def add(self, key: int) -> None:
        if not self.contains(key): # Check if the key is not already present in the set
            self.set.append(key) # Add the key to the set if it's not already present

    def remove(self, key: int) -> None:
        if self.contains(key): # Check if the key is present in the set
            self.set.remove(key) # Remove the key from the set if it exists
        

    def contains(self, key: int) -> bool:
        return key in self.set # Return True if the key is in the set, False otherwise


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)