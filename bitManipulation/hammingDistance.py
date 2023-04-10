# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        result = 0

        while x or y:
            last_bit_x = x&1
            last_bit_y = y&1

            result += last_bit_x ^ last_bit_y

            x = x >> 1
            y = y >> 1

        return result
            