import random

class RandomizedSet:

    def __init__(self):
        self.set = {}
        self.setlist = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        
        self.set[val] = len(self.setlist)
        self.setlist.append(val)
        return True

        
    def remove(self, val: int) -> bool:
        if val in self.set:            
            self.setlist[self.set[val]] = self.setlist[-1]
            self.set[self.setlist[-1]] = self.set[val]
            
            del self.set[val]
            self.setlist.pop()          
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.setlist)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()