# https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import List
from math import sqrt

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        lookup = {num:1 for num in nums}

        for num in nums:
            
            if sqrt(num) in lookup:
                lookup[num] = lookup[sqrt(num)]+1

        length = max(lookup.values())
        return length > 1 and length or -1