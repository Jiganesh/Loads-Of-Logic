# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from collections import defaultdict
from typing import List

class Solution:
    
    # Runtime: 2423 ms, faster than 100.00% of Python3 online submissions for Max Sum of a Pair With Equal Sum of Digits.
    # Memory Usage: 29.6 MB, less than 100.00% of Python3 online submissions for Max Sum of a Pair With Equal Sum of Digits.
    
    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        
        def helper(num):
            return sum([int(i) for i in str(num)])
        
        for i in nums:
            
            sum_of_num =  helper(i)
            d[sum_of_num].append(i)
            
        ans = -1
        for key, value in d.items():
            if len(value)>=2:
                ans = max(ans,sum(sorted(value)[-2:]))
                
        return ans
                
        
