# https://leetcode.com/problems/design-hashset/

class MyHashSet:
    
    # Runtime: 1406 ms, faster than 19.99% of Python3 online submissions for Design HashSet.
    # Memory Usage: 18.4 MB, less than 88.99% of Python3 online submissions for Design HashSet.

    def __init__(self):
        
        self.collection = []
        
        

    def add(self, key: int) -> None:
        
        if not self.contains(key):
            self.collection.append(key)
        

    def remove(self, key: int) -> None:
        
        if self.contains(key):
            self.collection.remove(key)
        

    def contains(self, key: int) -> bool:
        
        return key in self.collection
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class MyHashSet:
    
    # Runtime: 415 ms, faster than 35.28% of Python3 online submissions for Design HashSet.
    # Memory Usage: 40.6 MB, less than 10.21% of Python3 online submissions for Design HashSet.

    def __init__(self):
        
        self.collection = [False]* (10**6+1)
        
        

    def add(self, key: int) -> None:
        
        self.collection[key]= True
        

    def remove(self, key: int) -> None:
        
        self.collection[key] = False
        

    def contains(self, key: int) -> bool:
        
        return self.collection[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)