# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        max_heap = []
        for pile in piles:
            heapq.heappush(max_heap, -pile)


        while k:
            value = -heapq.heappop(max_heap)
            value = (value+1)//2
            heapq.heappush(max_heap, -value)
            k-=1

        return -sum(max_heap)
       