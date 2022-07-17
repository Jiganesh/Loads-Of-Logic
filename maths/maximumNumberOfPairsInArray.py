# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

from itertools import Counter
from typing import List

class Solution:
    
    # Runtime: 49 ms, faster than 69.23% of Python3 online submissions for Maximum Number of Pairs in Array.
    # Memory Usage: 13.8 MB, less than 92.31% of Python3 online submissions for Maximum Number of Pairs in Array.
    
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        pairs = 0
        leftover = 0
        
        for _ , value in d.items():
            pairs+= value//2
            leftover+=value%2
            
        return [pairs, leftover]