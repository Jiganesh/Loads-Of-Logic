# https://leetcode.com/problems/binary-number-with-alternating-bits/
class Solution:
    
    # Runtime: 31 ms, faster than 85.56% of Python3 online submissions for Binary Number with Alternating Bits.
    # Memory Usage: 13.9 MB, less than 54.95% of Python3 online submissions for Binary Number with Alternating Bits.
    def hasAlternatingBits(self, n: int) -> bool:
        
        tracker = n&1
        
        while n:
            
            lastbit = n&1
            if lastbit != tracker: return False
            
            #removing last bit as we have already checked it
            n = n>>1
            
        
            # toggling tracker for alternating effect
            tracker ^= 1
            
        return True