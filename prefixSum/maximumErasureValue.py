# https://leetcode.com/problems/maximum-erasure-value/

from collections import accumulate
import operator


# Prefix Sum and Longest Substring without Repeating Characters.
class Solution:
    
    # Runtime: 1368 ms, faster than 82.71% of Python3 online submissions for Maximum Erasure Value.
    # Memory Usage: 27.2 MB, less than 89.50% of Python3 online submissions for Maximum Erasure Value.

    # TC : O(N log N)
    # SC : O(N)
    def maximumUniqueSubarray(self, nums) :
        
        
        left = score = 0
        lookup = {}
        
        
        prefix_sum = [0]+list(accumulate(nums,operator.add))
        
        for right , i in enumerate(nums):
            
            if i in lookup:
                left = max(lookup[i]+1, left)
            
            lookup[i]= right
            score = max(score , prefix_sum[right+1]-prefix_sum[left])
            
    
        return score            