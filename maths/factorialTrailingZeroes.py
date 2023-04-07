# https://leetcode.com/problems/factorial-trailing-zeroes/
# Why Math works - http://mathandmultimedia.com/2014/01/25/zeros-are-there-in-n-factorial/

class Solution:
    
    def trailingZeroes(self, n: int) -> int:
        result = 0
        num = 5
        exp = 1
        while num**exp <= n:
            result += n// (num**exp)
            exp+=1
        return result

