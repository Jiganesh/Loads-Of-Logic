# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

from typing import List

class Solution:
    # Runtime: 2541 ms, faster than 40.90% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
    # Memory Usage: 48.3 MB, less than 71.48% of Python3 online submissions for Minimum Operations to Make a Uni-Value Grid.
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        
        R = len(grid)
        C = len(grid[0])
        
        maximum_in_grid = float("-inf")
        minimum_in_grid = float("inf")
        
        
        array = []
        
        for i in range(R):
            for j in range (C):
                
                maximum_in_grid = max(maximum_in_grid, grid[i][j]%x)
                minimum_in_grid = min(minimum_in_grid, grid[i][j]%x)
                
                array.append(grid[i][j] // x)
                
        
        if maximum_in_grid != minimum_in_grid : return -1
        
        median = sorted(array)[len(array)//2]
        return sum([abs(median-i) for i in array])
                
                
                