# https://leetcode.com/problems/perfect-squares/

import math

class Solution:

    # Runtime: 5958 ms, faster than 29.50% of Python3 online submissions for Perfect Squares.
    # Memory Usage: 14.2 MB, less than 51.71% of Python3 online submissions for Perfect Squares.
    
    def numSquares(self, n: int) -> int:
        denominations = [ i**2 for i in range (1, int(math.sqrt(n))+1)]
        
        dp = [n+1]*(n+1) 
        
        dp[0]=0
    
        for i in range (1, len(denominations)+1):
            for j in range (1, n+1 ):
                if denominations[i-1] <= j:
                    dp[j] = min(dp[j], 1+dp[j-denominations[i-1]])
                
        return dp[-1]