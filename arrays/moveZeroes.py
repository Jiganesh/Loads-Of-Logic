# https://leetcode.com/problems/move-zeroes/


class Solution:
    #     Runtime: 152 ms, faster than 99.86% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 15.6 MB, less than 19.78% of Python3 online submissions for Move Zeroes.
    def moveZeroes(self, nums: list[int]) -> None:
        index, end = 0, len(nums)
        for i in range(end):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        while index < end:
            nums[index] = 0
            index += 1
