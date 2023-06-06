# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        
        result = []
        for i in range (C):
            width = 0
            for j in range(R):
                width = max(width, len(str(grid[j][i])))
            result.append(width)
        return result
                