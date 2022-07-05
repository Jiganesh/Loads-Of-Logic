# https://leetcode.com/problems/maximum-gap/

from typing import List
import heapq

class Solution:
    
    # Runtime: 1155 ms, faster than 85.88% of Python3 online submissions for Maximum Gap.
    # Memory Usage: 24.6 MB, less than 99.79% of Python3 online submissions for Maximum Gap.
    def maximumGap(self, nums: List[int]) -> int:
        
        
        heapq.heapify(nums)
        
        start = nums[0]
        
        
        maxLength = 0
        while nums:
            end = heapq.heappop(nums)
            maxLength = max(maxLength, end-start)
            start = end
            
        return maxLength
            
            
        