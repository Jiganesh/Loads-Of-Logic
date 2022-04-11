# https://leetcode.com/problems/shift-2d-grid/

class Solution:
    
    # [All Three Accepted]
    
    # Runtime: 160 ms, faster than 96.38% of Python3 online submissions for Shift 2D Grid.
    # Memory Usage: 14.4 MB, less than 35.10% of Python3 online submissions for Shift 2D Grid.
    
    
    # TC : O(M*N)
    # SC : O(M*N)
    
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
    
    
    # TC : O(M*N)
    # SC : O(M*N)
    def shiftGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        start = m * n - k % (m * n)
        ans = []
        for i in range(start, m * n + start):
            j = i % (m * n)
            r, c =  j // n, j % n
            if not (j - start) % n:
                ans.append([])
            ans[-1].append(grid[r][c]) 
        return ans

    
    # TC : O(M*N)
    # SC : O(1)
    def shiftGrid(self, grid,k) :
        
        row = len(grid)
        column = len(grid[0])
        totalLength = (row*column)-1  # Pointer on Last Element
        
        k%=(row*column)
        
        def reverse (start , end):
            
            while start < end :
                
                startrow, startcol = (start//column)%row  , start%column
                endrow, endcol = (end//column)%row, end%column
                                
                grid[startrow][startcol] , grid[endrow][endcol] = grid[endrow][endcol], grid[startrow][startcol]
                
                start+=1
                end -=1
                
            return grid
                
        reverse(0, totalLength-k)
        reverse(totalLength-k+1 , totalLength)
        reverse(0, totalLength)
        
        
        return grid
    