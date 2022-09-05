# https://leetcode.com/problems/maximum-rows-covered-by-columns/
# Can be solved with bit mask also

from typing import List

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:

        
        R = len(mat)
        C = len(mat[0])
        
        
        # Step 1
        # Generate All possible combinations of cols column
        
        col_combinations = []
        def generate_col_combinations(ind, cols, combination):
            if cols==0:
                col_combinations.append(combination.copy())
                
            for i in range(ind+1, C):
                combination.add(i)
                generate_col_combinations(i, cols-1, combination )
                combination.remove(i)
                
        generate_col_combinations(-1, cols, set())
        
        
        # Step 2
        # For every combination check how many rows are covered and return the maximum result 
        
        result = 0
        for columns_covered in col_combinations:
            how_many_rows_are_covered = 0
            
            for i in range (R):
                row_covered = True
                
                for j in range(C):
                    
                    if mat[i][j]==1 and j not in columns_covered:
                        row_covered = False
                        
                how_many_rows_are_covered += row_covered
                
            result = max(result , how_many_rows_are_covered)
            
        return result
    