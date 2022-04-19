# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:
    
    # Runtime: 1528 ms, faster than 89.41% of Python3 online submissions for Range Sum Query 2D - Immutable.
    # Memory Usage: 26 MB, less than 17.78% of Python3 online submissions for Range Sum Query 2D - Immutable.

    def __init__(self, matrix):
        
        self.matrix = matrix
        
        rows = len(self.matrix)+1
        cols = len(self.matrix[0])+1
        self.lookupArray = [[0]*cols for i in range (rows)]
    
        for i in range (1, rows):
            for j in range (1, cols):
                
                self.lookupArray[i][j] = self.lookupArray[i][j-1]+self.matrix[i-1][j-1]
                
        for i in range (1, rows):
            for j in range (1, cols):
                
                self.lookupArray[i][j] = self.lookupArray[i-1][j]+self.lookupArray[i][j]
                
        for i in self.lookupArray:
            print(*i)
                
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        a = self.lookupArray[row2+1][col2+1]
        b = self.lookupArray[row1][col2+1]
        c = self.lookupArray[row2+1][col1]
        d = self.lookupArray[row1][col1]
        
        
        return a-b-c+d
    
        """
        -------------------
        |  |  |  |  |  |  |
        -------------------
        | d|  |  |  | b|  |
        -------------------
        |  |  |  |  |  |  |
        -------------------
        | c|  |  |  | a|  |
        -------------------
        """
        
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)