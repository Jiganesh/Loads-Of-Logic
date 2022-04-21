# https://leetcode.com/problems/design-hashmap/

class MyHashMap:
    
    # Runtime: 396 ms, faster than 47.21% of Python3 online submissions for Design HashMap.
    # Memory Usage: 40.4 MB, less than 5.22% of Python3 online submissions for Design HashMap.
    def __init__(self):
        
        self.collection = [-1]* (10**6+1)
        

    def put(self, key: int, value: int) -> None:
        
        self.collection [key] = value

    def get(self, key: int) -> int:
        
        return self.collection [key] 
        

    def remove(self, key: int) -> None:
        
        self.collection[key]= -1
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
STUFF YOU SHOULD GO THROUGH


https://leetcode.com/problems/design-hashmap/discuss/186443/Why-didn't-anyone-consider-load-factorrehash
https://leetcode.com/problems/design-hashmap/discuss/1968848/Pyrhon3-oror-Knuth's-multiplicative-method

"""