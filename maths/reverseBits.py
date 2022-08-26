# https://leetcode.com/problems/reverse-bits/

class Solution:

    # Runtime: 48 ms, faster than 60.64% of Python3 online submissions for Reverse Bits.
    # Memory Usage: 13.9 MB, less than 8.01% of Python3 online submissions for Reverse Bits.
    
    def reverseBits(self, n: int) -> int:
        
        result = 0
        
        for _ in range (32):
            
            last_bit = n & 1
            result = ( result << 1 )  | last_bit
            
            n = n >> 1
            
        return result 