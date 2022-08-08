# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

from typing import List

class Solution:
    
    # Runtime: 1731 ms, faster than 14.29% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    # Memory Usage: 103.3 MB, less than 42.86% of Python3 online submissions for Check if There is a Valid Partition For The Array.
    
    def validPartition(self, nums: List[int]) -> bool:
        
        dp ={}
        
        def helper (index):
            
            if index in dp:
                return dp[index]
            
            if index>=len(nums):
                dp[index]=True
                return True
            
            ans_1 = ans_2 = False
            
            if index+1< len(nums) and nums[index]==nums[index+1]:
                ans_1 = True and helper(index+2)
            
            if index+2 < len(nums) and (nums[index]==nums[index+1]==nums[index+2] or (nums[index+1]-nums[index]==1 and nums[index+2]-nums[index+1]==1)):
                ans_2 = True and helper(index+3)
              
            dp [index] = ans_1 or ans_2
            
            return dp[index]
        
        
        return helper(0)