# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

from typing import List

class Solution:
    # Runtime: 892 ms, faster than 70.01% of Python3 online submissions for Maximum Consecutive Floors Without Special Floors.
    # Memory Usage: 28 MB, less than 87.59% of Python3 online submissions for Maximum Consecutive Floors Without Special Floors.
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        
        
        special.sort()
        
        start = bottom
        end = special[0]
        
        index = 0
        
        max_consecutive = float("-inf")
        
        while end < top:
            
            max_consecutive = max(max_consecutive, end-start)
            start = end+1
            index+=1
            end =  special[index] if index< len(special) else top+1
            
        return max(max_consecutive, end-start)
    