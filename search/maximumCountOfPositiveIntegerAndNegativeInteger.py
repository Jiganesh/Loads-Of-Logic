# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

from typing import List

class Solution:
    
    # TC : O(N)
    # SC : O(1)
    def maximumCount(self, nums: List[int]) -> int:
        
        positive = 0
        negative = 0
        
        for i in nums:
            if i>0: positive+=1
            if i<0: negative+=1
        
        return max(positive, negative)

    # TC : O(logN)
    # SC : O(1)
    def maximumCount(self, nums: List[int]) -> int:
        
        l= bisect.bisect_left(nums, 0)
        r = bisect.bisect_right(nums, 0)
        return max(l,len(nums)-r)
        