from itertools import accumulate
from collections import defaultdict
from typing import List
import operator


class Solution:
    
    # Brute Force Solution
    # TC: O(N* (upper - lower))
    # SC : O(N)
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        prefix_sum_nums = [0] + list(accumulate(nums, operator.add))
        
        lookup = defaultdict(int)
        result = 0
        
        for curr_sum in prefix_sum_nums:
            for target in range (lower , upper+1):
                
                # target = right - left
                # left = right - target
                
                result += lookup[curr_sum-target]
                
            lookup[curr_sum]+=1
            
                
        return result