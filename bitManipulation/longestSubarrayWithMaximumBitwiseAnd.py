# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    
    # Runtime: 990 ms, faster than 87.83% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
    # Memory Usage: 28.2 MB, less than 93.07% of Python3 online submissions for Longest Subarray With Maximum Bitwise AND.
    
    def longestSubarray(self, nums):
        
        maximum_and = max(nums)
        
        count , max_count = 0 , 0
        
        for num in nums:
            if num == maximum_and:
                count+=1
            else:
                count=0
            max_count = max(max_count, count)
            
        return max_count
    
