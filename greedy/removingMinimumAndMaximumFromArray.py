# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/
from typing import List

class Solution:

    # Runtime: 1017 ms, faster than 79.43% of Python3 online submissions for Removing Minimum and Maximum From Array.
    # Memory Usage: 27.5 MB, less than 72.24% of Python3 online submissions for Removing Minimum and Maximum From Array.
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = j = 0
        
        for k in range (len(nums)):
            if nums[i]<nums[k]:
                i = k
            if nums[j]>nums[k]:
                j = k
                
        # i is index of maximum number and j is index of minimum number
        
        both_on_left = max(i+1, j+1)
        both_on_right = max(n-i, n-j)
        max_on_left_and_min_on_right = i+1 + n-j
        max_on_right_and_min_on_left = n-i + j+1
        
        return min(both_on_left, both_on_right, max_on_left_and_min_on_right, max_on_right_and_min_on_left)
        
        
        