# https://leetcode.com/problems/find-original-array-from-doubled-array/

from typing import List
from collections import Counter

class Solution:
    
    # Runtime: 1404 ms, faster than 96.60% of Python3 online submissions for Find Original Array From Doubled Array.
    # Memory Usage: 31.3 MB, less than 85.69% of Python3 online submissions for Find Original Array From Doubled Array.
    def findOriginalArray(self, changed: List[int]) -> List[int]:
           
        changed.sort()
        
        if len(changed)%2 !=0:
            return []
        
        lookup = Counter(changed)

        for num in sorted(lookup):
            if lookup[num] > lookup[num*2]:
                return []
            lookup[num*2]-= lookup[num] if num else lookup[num]//2
        
        return lookup.elements()