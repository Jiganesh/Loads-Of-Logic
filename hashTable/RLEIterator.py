# https://leetcode.com/problems/rle-iterator/

# Naive Approach 

# TC : O(C * K) where c is count of key and k is key
# SC : O(C * K) 
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.queue = deque([])
        n = len(encoding)

        for i in range (0,n, 2):
            self.queue.extend([encoding[i+1]] * (encoding[i]))

        print(self.queue)

        

    def next(self, n: int) -> int:
        while self.queue and n:
            val = self.queue.popleft()
            n-=1

        if n and not self.queue:
            return -1
        else:
            return val

# Better Approach
# TC : O(K) K is number of keys
# SC : O(K)
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.count_tracker = []
        self.value_tracker = []

        n = len(encoding)
        for i in range (0,n,2):
            self.count_tracker.append(encoding[i])
            self.value_tracker.append(encoding[i+1])

        self.pointer = 0
        

    def next(self, n: int) -> int:
        if self.pointer >= len(self.count_tracker):
            return -1
        
        count = self.count_tracker[self.pointer]
        if count < n:
            n-=self.count_tracker[self.pointer]
            self.count_tracker[self.pointer] = 0
            self.pointer+=1
            return self.next(n)
        else:
            self.count_tracker[self.pointer]-=n
            return self.value_tracker[self.pointer]
            

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)