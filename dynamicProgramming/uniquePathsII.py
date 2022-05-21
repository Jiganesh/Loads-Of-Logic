# https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    
    # Runtime: 39 ms, faster than 47.68% of Python online submissions for Unique Paths II.
    # Memory Usage: 13.7 MB, less than 11.84% of Python online submissions for Unique Paths II.
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int:
        
        """
        
        def helper (i, j ):
            
            if i<R and j<C and dp[i][j]!=-1:
                return dp[i][j]
            
            if i==R-1 and j==C-1 and obstacleGrid[i][j]==0:
                return 1
            
            if valid (i, j):
                ans = helper(i+1, j)+ helper(i, j+1)
                dp[i][j]= ans
                return dp[i][j]
            else : 
                return 0
            
            
        def valid(i, j):
            return 0<=i<R and 0<=j<C and obstacleGrid[i][j]==0
            
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        
        dp = [[-1]*C for i in range (R)]
            
        return helper(0,0)