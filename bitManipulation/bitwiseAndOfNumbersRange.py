# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        sc = 0
        while left and right and left != right:
            left >>=  1
            right >>= 1
            
            sc += 1
        return left << sc

