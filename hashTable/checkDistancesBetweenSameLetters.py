# https://leetcode.com/problems/check-distances-between-same-letters/
from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        lookup = {}
        
        for ind, ch in enumerate(s):
            
            if ch in lookup and ind-lookup[ch]-1 != distance[ord(ch)-ord("a")]:
                return False
            
            lookup[ch]=ind
            
        return True
