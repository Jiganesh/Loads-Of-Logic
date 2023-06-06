# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        def isvalid(i, j):
            return 0<=i<row and 0<=j<col

        def helper(i, j):

            # If the index is valid
            if isvalid(i,j):

                if grid[i][j] == 0:
                    grid[i][j]=2
                    up = helper(i-1, j)
                    down = helper(i+1, j)
                    left = helper(i, j-1)
                    right = helper(i, j+1)
                    return up and down and left and right
                return True

            return False

        count = 0
      
        for i in range (row):
            for j in range (col):
                # If it is land and surrounded by water count
                if grid[i][j] == 0 and helper(i, j):
                    count += 1
        return count