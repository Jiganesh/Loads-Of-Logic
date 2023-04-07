# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        def isvalid(i, j):
            return 0<=i<R and 0<=j<C

        def dfs (i, j):

            if isvalid(i,j) and grid[i][j] == 1:
                grid[i][j] = 0 
                dfs(i-1, j) # up
                dfs(i+1, j) # down
                dfs(i, j-1) # left
                dfs(i, j+1) # right

        # Eliminate 1's who do not have a boundary 
        for i in range (R):
            for j in range(C):
                if ((i == 0 or i == R-1) or (j == 0 or j== C-1)) and grid[i][j]==1:
                    dfs(i,j)

        # Count the number of 1's
        result  = 0
        for i in range(R):
            for j in range(C):
                result += grid[i][j]

        return result
