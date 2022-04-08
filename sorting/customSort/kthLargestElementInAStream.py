# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import bisect
class KthLargest:
    
    # Runtime: 148 ms, faster than 47.01% of Python3 online submissions for Kth Largest Element in a Stream.
    # Memory Usage: 18.3 MB, less than 31.19% of Python3 online submissions for Kth Largest Element in a Stream.

    def __init__(self, k: int, nums):
        
        self.k = k
        self.nums = sorted(nums)
        
    def add(self, val: int) -> int:

        bisect.insort(self.nums, val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# SECOND SOLUTION

import heapq


class KthLargest:
    
    # Runtime: 127 ms, faster than 63.67% of Python3 online submissions for Kth Largest Element in a Stream.
    # Memory Usage: 18.4 MB, less than 31.19% of Python3 online submissions for Kth Largest Element in a Stream.

    def __init__(self, k: int, nums):
        
        self.k = k
        self.nums = []

        for i in nums:
            heapq.heappush(self.nums, i)
        
    
    def add(self, val: int) -> int:
        
        heapq.heappush(self.nums, val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
