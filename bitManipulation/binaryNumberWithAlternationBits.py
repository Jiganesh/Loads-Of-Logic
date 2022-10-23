# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:

    # TC : O(logN)
    # SC : O(1)    
    def hasAlternatingBits(self, n: int) -> bool:

        last_bit = n&1
        n = n>>1

        while n:
            if last_bit == n&1:
                return False
            else:
                last_bit^=1
                n = n>>1

        return True
