# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    # Runtime: 150 ms, faster than 53.54% of Python3 online submissions for Minimum Path Sum.
    # Memory Usage: 19.8 MB, less than 9.49% of Python3 online submissions for Minimum Path Sum.
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R = len(grid)
        C = len(grid[0])
        dp = {}
                
        def helper(i, j):
            
            ans = float("inf")
            
            if i==R-1 and j==C-1:
                return grid[i][j]
            
            elif 0<=i<R and 0<=j<C:
                
                if (i,j) in dp : return dp[(i,j)]
                
                ans = grid[i][j] + min(helper(i, j+1) , helper(i+1, j))
                
            dp[(i,j)]= ans
            return ans
                
            
        
        return helper(0,0)