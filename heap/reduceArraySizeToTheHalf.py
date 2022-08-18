# https://leetcode.com/problems/reduce-array-size-to-the-half/

from typing import List
from collections import Counter
import heapq

class Solution:
    # Runtime: 649 ms, faster than 89.07% of Python3 online submissions for Reduce Array Size to The Half.
    # Memory Usage: 32.3 MB, less than 57.69% of Python3 online submissions for Reduce Array Size to The Half.
    def minSetSize(self, arr: List[int]) -> int:
        dictionary = Counter(arr)
        
        n = len(arr)
        half = n//2
        
        heap = [-value for key, value in dictionary.items()]
        heapq.heapify(heap)
        
        count = 0
        while n > half:
            n += heapq.heappop(heap)
            count+=1
            
        return count