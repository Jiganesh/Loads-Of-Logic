# https://leetcode.com/problems/fibonacci-number/

class Solution:
    # Runtime: 26 ms, faster than 98.16% of Python3 online submissions for Fibonacci Number.
    # Memory Usage: 13.8 MB, less than 95.78% of Python3 online submissions for Fibonacci Number.
    
    def fib(self, n: int) -> int:
        
        a,b=0,1
        for _ in range (n):
            a,b=b,a+b
        return a
                