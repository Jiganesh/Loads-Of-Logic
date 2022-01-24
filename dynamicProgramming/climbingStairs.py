 
# https://leetcode.com/problems/climbing-stairs

class Solution(object):
    
    # Using recursion (brute Force)- Not efficient 
    # Will give TLE
    
    # TC : O(N!)
    # SC : O(N)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=1 :
            return 1
        else :
            return self.climbStairs(n-1)+self.climbStairs(n-2)
        
    
    # TC :O(N)
    # SC : O(N)    
    def climbStairs (self,n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*(n+1)
        for i in range(2, n+1):
            dp[i]= dp[i-1]+dp[i-2]
        return dp[n]
    
    #TC : O(N)
    #SC : O(1)
    
    # Runtime: 20 ms, faster than 56.28% of Python online submissions for Climbing Stairs.
    # Memory Usage: 13.2 MB, less than 88.62% of Python online submissions for Climbing Stairs.
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=1,1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b

        
        
        
    
        
        
    