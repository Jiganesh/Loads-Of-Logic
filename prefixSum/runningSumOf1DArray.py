# https://leetcode.com/problems/running-sum-of-1d-array/

from itertools import accumulate
import operator


class Solution:
    
    # Runtime: 40 ms, faster than 89.27% of Python3 online submissions for Running Sum of 1d Array.
    # Memory Usage: 14.2 MB, less than 29.22% of Python3 online submissions for Running Sum of 1d Array.
    def runningSum(self, nums) :
        
        return list(accumulate(nums, operator.add))