# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

from typing import List

class Solution:
    
    # TC : O(N^2)
    # SC : O(N)
    
    # Runtime: 3870 ms, faster than 56.19% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    # Memory Usage: 14.2 MB, less than 57.52% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
    
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1
        # Find longest Increasing subsequence 
        lcs = [1]*n
        
        for pointer in range (n):
            for check in range (pointer):
                if nums[check]< nums[pointer]:
                    lcs[pointer] = max(lcs[pointer], lcs[check]+1)
        # print(lcs)
        
        # Step2
        # Find longes decreasing Subsequence
        lds = [1]*n
        
        for pointer in range(n-1,-1,-1):
            for check in range (pointer):
                if nums[check] > nums[pointer]:
                    lds[check] = max(lds[check], lds[pointer]+1)
        # print(lds)
        
        max_elements_present_to_make_mountain = 0
        for ind in range (n):
            if lcs[ind]>1 and lds[ind]>1:
                max_elements_present_to_make_mountain = max(lcs[ind]+lds[ind]-1 , max_elements_present_to_make_mountain)
        
        return n- max_elements_present_to_make_mountain
                
                
        