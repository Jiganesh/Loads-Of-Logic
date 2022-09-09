# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

from typing import List

class Solution:
    # Runtime: 1408 ms, faster than 12.90% of Python3 online submissions for Count Square Submatrices with All Ones.
    # Memory Usage: 16.3 MB, less than 73.99% of Python3 online submissions for Count Square Submatrices with All Ones.
    def countSquares(self, matrix: List[List[int]]) -> int:
            
        dp = matrix[:]
        
        R = len(matrix)
        C = len(matrix[0])
        
        
        for r in range(1, R):
            for c in range(1, C):
                
                if dp[r][c]==1:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    
            
        total_squares = 0
        
        for r in range (R):
            for c in range(C):
                
                total_squares+= dp[r][c]
                
        return total_squares
    
    # Optimized Run TIme
    
    # Runtime: 611 ms, faster than 96.57% of Python3 online submissions for Count Square Submatrices with All Ones.
    # Memory Usage: 16.4 MB, less than 15.95% of Python3 online submissions for Count Square Submatrices with All Ones.
    
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        
        dp = matrix[:]
        
        R = len(matrix)
        C = len(matrix[0])
        
        total_squares = 0
        
        for r in range(0, R):
            for c in range(0, C):
            
                
                if r!=0 and c!=0 and dp[r][c]==1:
                    
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    
                total_squares+= dp[r][c]
                
        return total_squares

