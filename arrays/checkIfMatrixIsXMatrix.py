# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
from typing import List

class Solution:
    # Runtime: 265 ms, faster than 100.00% of Python3 online submissions for Check if Matrix Is X-Matrix.
    # Memory Usage: 14.9 MB, less than 100.00% of Python3 online submissions for Check if Matrix Is X-Matrix.
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        X = len(grid)
    
        for i in range (X):
            for j in range(X):
                
                if (i-j ==0 or i+j==X-1) and grid[i][j] ==0:
                    return False
                elif not (i-j==0 or i+j==X-1) and grid[i][j]!=0:
                    return False
                
        return True
    
    
