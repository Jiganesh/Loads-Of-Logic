# https://leetcode.com/problems/maximum-strong-pair-xor-i/

class Solution:

    # TC: O(N^2)
    # SC: O(1)
    
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        result = 0
        
        for x in nums : 
            for y in nums:
                if abs(x-y) <= min(x,y):
                    result = max(result, x^y)
        return result