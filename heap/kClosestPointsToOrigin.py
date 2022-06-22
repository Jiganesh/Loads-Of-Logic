# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq



class Solution:
    
    # TC : O(N* logK)
    # SC : O(N) 
       
    # Runtime: 1306 ms, faster than 30.15% of Python3 online submissions for K Closest Points to Origin.
    # Memory Usage: 20.4 MB, less than 59.17% of Python3 online submissions for K Closest Points to Origin.
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        
        for x, y in points:
            heapq.heappush(heap, (-(x**2 + y**2)**0.5, x, y))
            
            if len(heap)>k:
                heapq.heappop(heap)
                
        result = []
        for i in heap:
            d, x, y = i
            result. append([x, y])
        
        return result 
    
    
    