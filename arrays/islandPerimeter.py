# https://leetcode.com/problems/island-perimeter/

from typing import List

class Solution:


    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 745 ms, faster than 62.89% of Python3 online submissions for Island Perimeter.
    # Memory Usage: 14.4 MB, less than 47.11% of Python3 online submissions for Island Perimeter.
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        perimeter = 0


        def valid (i, j):
            return 0<=i<R and 0<=j<C

        for i in range (R):
            for j in range (C):
                if grid[i][j]:
                    
                    up = grid[i-1][j] if valid(i-1,j) else 0
                    down = grid[i+1][j] if valid(i+1,j) else 0
                    left = grid[i][j-1] if valid(i,j-1) else 0
                    right = grid[i][j+1] if valid(i,j+1) else 0

                    perimeter +=  grid[i][j]*4 - (up + down + left + right)

        return perimeter