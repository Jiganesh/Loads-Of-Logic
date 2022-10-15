# https://leetcode.com/problems/score-after-flipping-matrix/

from typing import List

class Solution:
    
    # TC : O(R*C)
    # SC : O(R)
    def matrixScore(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        for i in grid:
            print(*i)

        print("-----------")

        def flipping_row(row):
            
            for col in range (C):
                grid[row][col] ^= 1

        def flipping_col(col):

            for row in range (R) :
                grid[row][col] ^= 1

        # Going Greedy 

        # Step 1 
        # We will get maximum value in there are all 1 where col = 0

        for row in range (R):
            if grid[row][0] != 1:
                flipping_row(row)

        
        # Step 2
        # We will check all column we need max set bits in all columns

        for col in range (1, C):
            set_bits = 0
            for row in range (R):
                set_bits+= grid[row][col]

            if set_bits <= R//2:
                flipping_col(col)


        for i in grid:
            print(*i)
        
        result_sum = 0
        for row in grid:
            result_sum += int( "".join(map(str, row)), 2)

        return result_sum
            

        