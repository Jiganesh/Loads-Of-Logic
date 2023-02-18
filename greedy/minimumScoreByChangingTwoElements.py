# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        nums.sort()

        # smallest two numbers are changed
        a = nums[-1]- nums[2]

        # largest two numbers are changed
        b = nums[-3]-nums[0]

        # smallest and largest number is changed
        c = nums[-2] - nums[1]

        return min(a, b , c)
