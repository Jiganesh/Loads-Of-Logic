# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List

class Solution:
    
    # Runtime: 342 ms, faster than 90.03% of Python3 online submissions for Longest Consecutive Sequence.
    # Memory Usage: 28.6 MB, less than 42.76% of Python3 online submissions for Longest Consecutive Sequence.
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        lookup = set(nums)
        
        result = 0 
        
        for start_num in lookup:
            
            if start_num-1  not in lookup:
                end_num = start_num
                
                while end_num+1 in lookup:
                    end_num+=1
                
                result = max(result, end_num-start_num+1)
                
        return result 
                
                