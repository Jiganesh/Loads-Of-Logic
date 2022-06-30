# https://leetcode.com/problems/rotate-image/


# REFER SOLUTION FROM NEETCODE : https://www.youtube.com/watch?v=fMSJSS7eO1w
from typing import List

class Solution:


    # TC : O(N*N)
    # SC : O(1)
        
    
    # Runtime: 38 ms, faster than 89.42% of Python3 online submissions for Rotate Image.
    # Memory Usage: 14.1 MB, less than 29.49% of Python3 online submissions for Rotate Image.
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        x = len(matrix)
        
        for i in range (x):
            for j in range (i, x):
                if i!=j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        
        for i in matrix:
            print(*i)
            
            
        l = 0
        r = x-1
        
        while l< r:
            for i in range(x):
                matrix[i][l] , matrix[i][r] = matrix[i][r], matrix[i][l]
                
            l+=1
            r-=1
                
        
            
                
    # TC : O(N*N) 
    # SC : O(1)
    
    # More Impressive Solution
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l = 0
        r = len(matrix)-1
        
        while l< r:
            
            top , bottom = l, r
            
            for i in range (r-l):
                
                top_left = matrix[top][l+i]
                
                matrix[top][l+i] = matrix[bottom-i][l]
                
                matrix[bottom-i][l] = matrix[bottom][r-i]
                
                matrix[bottom][r-i]= matrix[top+i][r]
                
                matrix[top+i][r] = top_left
                

            l+=1
            r-=1
                
                
    