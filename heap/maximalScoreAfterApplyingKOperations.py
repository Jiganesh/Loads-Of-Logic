# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

from typing import List
import heapq
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        while k:
            val = -heapq.heappop(max_heap)
            score+=val
            val = ceil(val/3.0)
            heapq.heappush( max_heap, -val)
            k-=1
            
        return score