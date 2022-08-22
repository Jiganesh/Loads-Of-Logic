# https://leetcode.com/problems/power-of-three/

class Solution:
    
    def isPowerOfThree(self, n: int) -> bool:

        return n>0  and 3**int(math.log10(n)/math.log10(3)) == n