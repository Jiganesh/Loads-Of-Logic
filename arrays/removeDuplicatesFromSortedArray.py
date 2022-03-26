# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Runtime: 138 ms, faster than 47.61% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 15.6 MB, less than 21.60% of Python3 online submissions for Remove Duplicates from Sorted Array.


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            nums[k] = nums[i]
            k += 1
        return k
