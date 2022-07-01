# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from typing import List

class Solution:
    
    # Runtime: 157 ms, faster than 12.32% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
    # Memory Usage: 15.2 MB, less than 95.33% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
    
    def minMoves2(self, nums: List[int]) -> int:
        
        median = sorted(nums)[len(nums)//2]
        return sum([abs(median-i) for i in nums])