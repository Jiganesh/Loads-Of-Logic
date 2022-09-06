# https://leetcode.com/problems/longest-nice-subarray/

from typing import List

class Solution:
    
    #  TC: O(N)
    #  SC: O(1)
    
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        left_ind = 0
        longest_subarray_length = 1
        
        bit_union = 0
        
        for right_ind in range(n):
            
            while bit_union & nums[right_ind] != 0:
                bit_union ^= nums[left_ind]
                left_ind += 1
                
            bit_union |= nums[right_ind]
            longest_subarray_length = max(longest_subarray_length, right_ind-left_ind+1)
            
        return longest_subarray_length
            
                