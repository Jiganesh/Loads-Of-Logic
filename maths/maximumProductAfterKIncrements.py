# https://leetcode.com/problems/maximum-product-after-k-increments/

import heapq

class Solution:
    
    # TC : O(N log N)
    # SC : O(N)
    
    # Runtime: 1864 ms, faster than 20.00% of Python3 online submissions for Maximum Product After K Increments.
    # Memory Usage: 24.7 MB, less than 10.00% of Python3 online submissions for Maximum Product After K Increments.
    def maximumProduct(self, nums, k) :
        
        # creating a heap
        heap = []
        for i in nums:
            heapq.heappush (heap,i)
            
            
        # basic idea here is keep on incrementing smallest number then only multiplication of that number will be greater
        # so basically till I have operations left I will increment my smallest number
        while k :
            current = heapq.heappop(heap)
            heapq.heappush(heap, current+1)
            k-=1
            
        result =1
        
        # Just Multiply all the numbers in heap and return the value
        while len(heap)>0:
            x= heapq.heappop(heap)
            result =(result*x )% (10**9+7)
            
        return result