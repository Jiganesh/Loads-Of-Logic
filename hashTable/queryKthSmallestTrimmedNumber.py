# https://leetcode.com/problems/query-kth-smallest-trimmed-number/

from collections import defaultdict
from typing import List


class Solution:
    
    # Runtime: 1714 ms, faster than 11.11% of Python3 online submissions for Query Kth Smallest Trimmed Number.
    # Memory Usage: 15.5 MB, less than 22.22% of Python3 online submissions for Query Kth Smallest Trimmed Number.

    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        d = defaultdict(list)
        for ind, num in enumerate(nums):
            for i in range (len(num)-1,-1,-1):
                d[len(num)-i].append((int(num[i:]),ind ))
                
        for i in d:
            d[i].sort()
            
        result = []
        
        for u, v in queries:
            result.append(d[v][u-1][1])
        return result
    
    