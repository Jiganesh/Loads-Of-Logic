# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    
    # TC: O(N)
    # SC: O(1)
    
    def xorOperation(self, n: int, start: int) -> int:

        xor = 0
        for i in range(n):
            xor ^= start+ (2*i)
        return xor