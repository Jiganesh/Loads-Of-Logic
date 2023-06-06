# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first, second, third = float("-inf"), float("-inf"), float("-inf")
        nums = set(nums)
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num

        return third if third != float("-inf") else first
            