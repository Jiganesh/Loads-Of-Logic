# https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
from typing import List

class Solution:
    
    # Runtime: 1013 ms, faster than 29.40% of Python3 online submissions for Furthest Building You Can Reach.
    # Memory Usage: 28.7 MB, less than 16.28% of Python3 online submissions for Furthest Building You Can Reach.
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        
        for index in range (len(heights)-1):
            
            gap =heights[index+1] - heights[index]
            
            if gap >0: heapq.heappush(heap, gap)
            
            if len(heap)> ladders:
                min_gap  = heapq.heappop(heap)
                bricks-=min_gap
                
            if bricks < 0 : 
                return index
                
        return len(heights)-1