# https://leetcode.com/problems/number-of-ways-to-split-array/submissions/ 
from itertools import accumulate
import operator

class Solution:
    
    # Runtime: 1370 ms, faster than 60.00% of Python3 online submissions for Number of Ways to Split Array.
    # Memory Usage: 29.3 MB, less than 20.00% of Python3 online submissions for Number of Ways to Split Array.
    def waysToSplitArray(self, nums) -> int:
        
        array = list(accumulate(nums, operator.add))
        count=0
        end = array[-1]
        for i in range (len(array)-1):
            
            left = array[i]-0
            right = end - array[i]
            
            if left >= right: count+=1
                
        return count
    
    # Runtime: 1110 ms, faster than 100.00% of Python3 online submissions for Number of Ways to Split Array.
    # Memory Usage: 29.4 MB, less than 20.00% of Python3 online submissions for Number of Ways to Split Array.
    def waysToSplitArray(self, nums) -> int:
        
        left, right, count = 0, sum (nums), 0

        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if left >=right :
                count+=1
                
        return count