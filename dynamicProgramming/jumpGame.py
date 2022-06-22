# https://leetcode.com/problems/jump-game/
# https://www.youtube.com/watch?v=muDPTDrpS28

from typing import List


class Solution:
    # Runtime: 1211 ms, faster than 13.81% of Python3 online submissions for Jump Game.
    # Memory Usage: 15.2 MB, less than 82.18% of Python3 online submissions for Jump Game.
    def canJump(self, nums: List[int]) -> bool:
    
        reachable = nums[0]
        
        for index , jump in enumerate(nums):
            if index>reachable : break
            reachable = max(index+jump, reachable)
        
        return reachable >= len(nums)-1