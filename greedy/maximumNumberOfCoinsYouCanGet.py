# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

from typing import List

class Solution:
    
    # TC : O(NlogN)
    # SC : O(1)
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()

        result = 0
        turns = len(piles)//3

        for turn in range(turns):
            piles.pop()
            result+=piles.pop()
        return result
    
    # One Liner
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])
        