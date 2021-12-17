#https://leetcode.com/problems/lru-cache/

class LRUCache:
    #logic: when we deal with an element / key:value append it to last, so first element will always be least recently used 

    def __init__(self, capacity: int):
        self.mapp={}
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.mapp.keys(): #if key is in mapp return value else -1
            popped=self.mapp.pop(key) 
            self.mapp.update({key:popped}) #dealt with this so append it to last
            return popped
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mapp.keys(): #if the key is already present

            self.mapp.pop(key) #pop it
            
        elif len(self.mapp)==self.cap: #when the size gets full, then remove lru which will be first element
            self.mapp.pop(next(iter(self.mapp))) #remove first key/value pair
            
        self.mapp.update({key:value}) #there is space remained so directly append


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)