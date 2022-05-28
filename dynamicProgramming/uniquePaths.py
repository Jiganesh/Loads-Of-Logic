# https://leetcode.com/problems/unique-paths/

class Solution:
    
    # Runtime: 41 ms, faster than 58.67% of Python3 online submissions for Unique Paths.
    # Memory Usage: 14 MB, less than 14.80% of Python3 online submissions for Unique Paths.
    
    def uniquePaths(self, m: int, n: int) -> int:

        def is_valid(i, j):
            return 0<=i<m and 0<=j<n
        
        dp = [[-1] * (n+1) for i in range(m+1)]
        
        def dfs (i, j):
            
            if dp[i][j] !=-1:
                return dp[i][j]
            
            if i==m-1 and j==n-1:
                return 1
            elif is_valid(i, j):
                
                ans = dfs(i, j+1) + dfs(i+1, j)
                dp[i][j] = ans
                return ans
            
            return 0
        
    
        return dfs(0,0)