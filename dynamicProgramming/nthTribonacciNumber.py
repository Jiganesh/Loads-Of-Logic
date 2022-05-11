# https://leetcode.com/problems/n-th-tribonacci-number/
class Solution:
    
    # Runtime: 52 ms, faster than 22.31% of Python3 online submissions for N-th Tribonacci Number.
    # Memory Usage: 13.9 MB, less than 13.48% of Python3 online submissions for N-th Tribonacci Number.
    
    
    # TC : O(N)
    # SC : O(1)
    
    def tribonacci(self, n: int) -> int:
        
        a, b, c = 0,1,1
        
        if n < 2: return a if n==0 else b if n==1 else c
        
        for i in range (n-2):
            a, b ,c  = b, c, a+b+c
            
        return c
        
        
        
        