# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

from typing import List

class Solution:
    # Runtime: 435 ms, faster than 28.62% of Python3 online submissions for Minimum Moves to Equal Array Elements.
    # Memory Usage: 15.2 MB, less than 95.09% of Python3 online submissions for Minimum Moves to Equal Array Elements.
    def minMoves(self, nums: List[int]) -> int:
        
        return sum(nums)-min(nums)*len(nums)
        