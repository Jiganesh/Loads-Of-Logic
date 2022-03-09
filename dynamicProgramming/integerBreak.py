# https://leetcode.com/problems/integer-break/
# DP Solution : https://www.youtube.com/watch?v=A-NALFDZCNs

import math
class Solution(object):
    
    # TC : O(N^2)
    # SC : O(N)
    
    # Using DP Appproach
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = {1: 1}
        def dfs(n):
            
            if n in dp : return dp[n]
            
            res = 0
            for i in range(1, n+1):
                ans = i * max(n-i, dfs(n-i))
                res = max(ans, res)
                
            dp[n]= res
            return res
        
        return dfs(n)
    
    # TC: O(1)
    # SC : O(1)
    
    # Runtime: 30 ms, faster than 43.21% of Python online submissions for Integer Break.
    # Memory Usage: 13.4 MB, less than 62.72% of Python online submissions for Integer Break.
    
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n<=1 : return 0
        if n ==2: return 1
        if n ==3 : return 2
        
        if n % 3==0:
            result= math.pow(3, n//3)
        if n %3 == 1:
            result= 2*2* math.pow(3, (n-4)//3)
        if n%3==2:
            result= 2*math.pow(3, (n-2)//3)
            
        return int(result)