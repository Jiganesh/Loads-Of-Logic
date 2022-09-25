# https://leetcode.com/problems/find-all-good-indices/
from typing import List

class Solution:
    
    # Runtime: 1123 ms, faster than 87.58% of Python3 online submissions for Find All Good Indices.
    # Memory Usage: 30.7 MB, less than 91.60% of Python3 online submissions for Find All Good Indices.
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        increasing_dp = [1]*n
        
        
        for ind, num in enumerate(nums):
            if ind>0 and nums[ind-1]>=nums[ind]:
                increasing_dp[ind] = increasing_dp[ind-1]+ 1
        
        decreasing_dp = [1]*n
        
        for ind in range (n-1, -1, -1):
            if ind<n-1 and nums[ind+1]>=nums[ind]:
                decreasing_dp[ind]= decreasing_dp[ind+1]+ 1 
        
        result = []
        # print(increasing_dp)
        # print(decreasing_dp)
        
        for i in range (1, n-1):
        
            if increasing_dp[i-1]>=k and decreasing_dp[i+1]>=k:
                result.append(i)
                
        return result