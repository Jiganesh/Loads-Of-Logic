# https://leetcode.com/problems/maximal-rectangle/

from typing import List

class Solution:
    
    # Runtime: 371 ms, faster than 70.11% of Python3 online submissions for Maximal Rectangle.
    # Memory Usage: 15.2 MB, less than 89.88% of Python3 online submissions for Maximal Rectangle.
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largest_rectangle(array, n):
            
            stack = []
            max_area = 0
            
            for curr_index, curr_height in enumerate(array):
                index  = curr_index
                while stack and stack[-1][1]>curr_height:
                    index, height = stack.pop()
                    area = (curr_index- index)*height
                    max_area = max(area, max_area)
                
                stack.append([index, curr_height])

            for curr_index, curr_height in stack:
                area = (n - curr_index)* curr_height
                max_area = max(area, max_area)
            
            return max_area
        
        R = len(matrix)
        C = len(matrix[0])
        
        result = 0
        
        level = [0]*C
        for r in range (R):
            
            for c in range(C):
                value = matrix[r][c]
                
                if value=="1":
                    level[c]+= int(value)
                else :
                    level[c]= 0
                    
            result = max(result , largest_rectangle(level, C))
            
        return result 
                
            