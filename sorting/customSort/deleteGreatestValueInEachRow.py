# https://leetcode.com/problems/delete-greatest-value-in-each-row/
from typing import List

class Solution:
    # TC : O(R*C+RlogR)
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        for row in grid:
            row.sort()

        R = len(grid)
        C = len(grid[0])

        result = 0
        for c in range(C):
            max_ele = float("-inf")
            for r in range(R):
                max_ele = max(max_ele, grid[r][c])
            result += max_ele            
        
        return result