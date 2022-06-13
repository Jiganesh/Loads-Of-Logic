class Solution:
    
    # Runtime: 2476 ms, faster than 71.43% of Python3 online submissions for Minimum Path Cost in a Grid.
    # Memory Usage: 20.1 MB, less than 100.00% of Python3 online submissions for Minimum Path Cost in a Grid.    
    
    def minPathCost(self, grid, moveCost):
        
        R = len(grid)
        C = len(grid[0])
        moveCostGrid = [[0] *C for i in range (R)]
        
        moveCostGrid[0]=grid[0]
        
        for i in range (1,R):
            for j in range (C):
                minCostForCell = float("inf")
                for k in range (C):
                    parent = grid[i-1][k]
                    # print(grid[i][j], parent,  moveCostGrid[i-1][k], moveCost[parent][j])
                    minCostForCell = min(minCostForCell, moveCostGrid[i-1][k]+ moveCost[parent][j])
                
                moveCostGrid[i][j] = grid[i][j]+minCostForCell
                
        return min(moveCostGrid[-1])
        