# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

from typing import List

class Solution:
    
    # TC = O(R*C)
    # SC = O(R+C)
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        row_max = [0]*R 
        col_max = [0]*C 

        for i in range (R):
            for j in range (C):

                row_max[i] = max(row_max[i], grid[i][j])
                col_max[j] = max(col_max[j], grid[i][j])

       
        maximum_total_sum = 0

        for i in range (R):
            for j in range (C):

                maximum_total_sum +=    min(row_max[i], col_max[j]) - grid[i][j]

        return maximum_total_sum
       