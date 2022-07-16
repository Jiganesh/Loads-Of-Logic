from typing import List

class Solution:
    
    # TC : O(m*n)
    # SC : O(m*n)+O(N)
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        R = len(grid)
        C = len(grid[0])
        
        matrix =[row[:] for row in grid]
        
        def helper(i, j, value):
            
            
            if valids(i, j) and grid[i][j]==value:
                
                grid[i][j] = ("*","*")
                
                helper(i+1, j ,value)
                helper(i-1, j,value)
                helper(i, j+1 ,value)
                helper(i, j-1 ,value)
              
        def valids (i, j):
            return 0<=i<R and 0<=j<C 
        
        def valid (i, j):
            return 0<=i<R and 0<=j<C and type(grid[i][j])==tuple
        
        
        helper(row, col , grid[row][col])
        
        for i in range (R):
            for j in range (C):
                
                if valid(i, j) and grid[i][j][0]=="*":
                    up = True if valid(i-1, j ) and grid[i-1][j][0] =="*" else False
                    down = True if valid (i+1,j) and grid[i+1][j][0]=="*" else False
                    left = True if valid(i,j+1) and grid[i][j+1][0] =="*" else False
                    right = True if valid (i, j-1) and grid[i][j-1][0] =="*" else False
                    
                    if up and down and left and right : grid[i][j]=("*",matrix[i][j])
                        
                        
        for i in range (R):
            for j in range (C):
                if type (grid[i][j])==tuple:
                    if grid[i][j][1]=="*":
                        grid[i][j]=color
                    else:
                        grid[i][j]=grid[i][j][1]
                        
        return grid
    
    # TC : O(m*n)
    # SC : O(N)

    # Elegant Code (Inspired from Pep Coding Logic)

    # Runtime: 189 ms, faster than 59.18% of Python3 online submissions for Coloring A Border.
    # Memory Usage: 14.4 MB, less than 25.71% of Python3 online submissions for Coloring A Border.
    
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        
        R = len(grid)
        C = len(grid[0])        
        
        def helper(i, j):
            
            
            if valid(i, j) and grid[i][j]== value:
                
                grid[i][j] = -grid[i][j]
                
                helper(i+1, j)
                helper(i-1, )
                helper(i, j+1)
                helper(i, j-1)
              
        def valid (i, j):
            return 0<=i<R and 0<=j<C 
        
        def check (x, y):
            return 1 if valid(x, y) and abs(grid[x][y])==value else 0
        
        value = grid[row][col]
        helper(row, col )
        
        for i in range (R):
            for j in range (C):
                
                if valid(i, j) and grid[i][j]<0:
                    up = check(i-1, j ) 
                    down = check (i+1,j) 
                    left = check(i,j+1) 
                    right = check (i, j-1)
                    
                    if (up+down+left+right)==4 : grid[i][j]=abs(grid[i][j])
                        
                        
        for i in range (R):
            for j in range (C):
                if grid[i][j] < 0:
                    grid[i][j] = color
                        
        return grid