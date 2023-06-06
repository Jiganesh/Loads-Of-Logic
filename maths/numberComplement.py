# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:

        result = 0
        step = 0

        if num ==0:
            return 1

        while num:
            
            last_bit = num&1
            result |= (last_bit ^ 1) << step
            num = num >> 1
            step += 1

        return result