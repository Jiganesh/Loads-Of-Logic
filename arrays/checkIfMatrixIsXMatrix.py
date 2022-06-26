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
    
    
    
print(Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
print(Solution().checkXMatrix([[6,0,0,0,0,0,0,18],[0,17,0,0,0,0,18,0],[0,0,13,0,0,17,0,0],[0,0,0,9,18,0,0,0],[0,0,0,2,20,0,0,0],[0,0,20,0,0,3,0,0],[0,14,0,0,0,0,11,0],[19,0,0,0,0,0,0,9]]
))
