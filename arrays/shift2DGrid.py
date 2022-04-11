# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    
    # Runtime: 160 ms, faster than 96.38% of Python3 online submissions for Shift 2D Grid.
    # Memory Usage: 14.4 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
    
    def shiftGrid(self, grid, k: int) :
                
        result = []
        
        for i in grid:
            for j in i:
                
                result.append(j)
                
        k=k%(len(grid)*len(grid[0]))             
        result = result [-k:]+ result [:-k]
        
        pointer=0
        
        for i in range (len(grid)):
            for j in range(len(grid[i])):
                grid[i][j]= result[pointer]
                pointer+=1
                
        return grid