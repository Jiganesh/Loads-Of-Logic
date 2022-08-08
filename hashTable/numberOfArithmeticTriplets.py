# https://leetcode.com/problems/number-of-arithmetic-triplets/

from typing import List

class Solution:
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 47 ms, faster than 50.00% of Python3 online submissions for Number of Arithmetic Triplets.
    # Memory Usage: 13.8 MB, less than 66.67% of Python3 online submissions for Number of Arithmetic Triplets.
    
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        set_num = set(nums)
        count=0
        for num in nums:
            if num+diff in set_num and num+(2*diff) in set_num:
                count+=1
                
        return count
        
