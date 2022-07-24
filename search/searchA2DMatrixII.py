# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List
class Solution:
    
    # Runtime: 189 ms, faster than 84.28% of Python3 online submissions for Search a 2D Matrix II.
    # Memory Usage: 20.5 MB, less than 13.29% of Python3 online submissions for Search a 2D Matrix II.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row , col = 0, len(matrix[0])-1
        while row<len(matrix) and  col>=0:
        
            pointing = matrix[row][col]
            if pointing == target : return True
            if pointing > target: col-=1
            else : row+=1
                
        return False