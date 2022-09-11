# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        
        group = []
        
        for start, end in intervals:
            
            if group and group[0] < start:
                heapq.heappop(group)
                heapq.heappush(group, end)
            else:
                heapq.heappush(group, end)
        
        return len(group)
