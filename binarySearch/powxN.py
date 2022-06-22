# https://leetcode.com/problems/powx-n/

class Solution:
    
    # Runtime: 56 ms, faster than 22.91% of Python3 online submissions for Pow(x, n).
    # Memory Usage: 13.8 MB, less than 97.72% of Python3 online submissions for Pow(x, n).

    def myPow(self, x: float, n: int) -> float:
        
        
        def helper(x, n):
            print(x, n)
            if n==0:
                return 1
            elif n < 0:
                return helper(1/x, -n)
            elif n%2 :
                return x* helper(x, n-1)
            
            return helper(x*x, n//2)
        
        return helper(x, n)
    
    
    # ITERATIVE
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow