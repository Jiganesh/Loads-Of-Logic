# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
    # Runtime: 27 ms, faster than 99.89% of Python online submissions for Min Cost Climbing Stairs.
    # Memory Usage: 13.6 MB, less than 55.39% of Python online submissions for Min Cost Climbing Stairs.
    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """        
        dp = [float("inf")]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        
        for i in range (2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2])+cost[i]
            
        return min(dp[-1], dp[-2])
    
    # Space Optimizeds    
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        a = cost[0]
        b = cost[1]
        
        for i in range(2,len(cost)):
            a, b = b, cost[i]+min(a,b)
            
        return min(a, b)