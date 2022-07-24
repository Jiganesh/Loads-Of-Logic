# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

import heapq
from typing import List

class Solution:
    # Runtime: 45 ms, faster than 75.82% of Python3 online submissions for Minimum Amount of Time to Fill Cups.
    # Memory Usage: 13.9 MB, less than 63.07% of Python3 online submissions for Minimum Amount of Time to Fill Cups.
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        for i in amount :
            heapq.heappush(heap, -i)
        
        count =0
        while heap[0]!=0:
            count+=1
            
            firstmaximum = heapq.heappop(heap)
            secondmaximum = heapq.heappop(heap)
            
            heapq.heappush(heap, min(0, firstmaximum+1))
            heapq.heappush(heap, min(0, secondmaximum+1))
        
        return count