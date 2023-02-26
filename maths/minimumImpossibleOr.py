# https://leetcode.com/problems/minimum-impossible-or

class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        result = 1
        while result in nums:
            result *=2
        return result
        