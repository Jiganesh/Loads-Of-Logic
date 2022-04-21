# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution(object):
    
    # Runtime: 12 ms, faster than 99.17% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
    # Memory Usage: 13.3 MB, less than 88.43% of Python online submissions for Minimum Value to Get Positive Step by Step Sum.
    
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        maximum = 1
        
        for index, i in enumerate (nums):
            result += nums[index]
            nums[index] = result
            
            maximum = max (maximum , 1- result)
           
        return maximum