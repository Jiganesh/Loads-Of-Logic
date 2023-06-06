# https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

class Solution:
    def minOperations(self, n: int) -> int:
        
        cnt = 0
        while n:
            exp = 1
            while 2**exp < n: exp += 1
            n = min(abs(2**exp - n), abs(2**(exp-1) - n))
            cnt += 1
        return cnt