# https://leetcode.com/problems/neither-minimum-nor-maximum/

class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        
        n = len(nums)

        if n <=2 : return -1

        return nums[n//2]

