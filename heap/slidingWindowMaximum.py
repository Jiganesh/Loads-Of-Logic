# https://leetcode.com/problems/sliding-window-maximum/


import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
            heap = []
            result = [] 
            for index  , num in enumerate(nums):
                heapq.heappush(heap, (-num, index))
                
                while heap and  heap[0][1] <= index-k:
                    heapq.heappop(heap)
                
                if index >= k-1:
                    result.append(-heap[0][0])
            return result
                    