# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/

class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        nums = [i%value for i in nums]
        lookup = Counter(nums)

        i = 0
        while lookup[i % value] > 0:
            lookup[i % value]-=1
            i+=1
        return i