# https://leetcode.com/problems/sort-the-matrix-diagonally/


import heapq
from typing import List
from collections import defaultdict


class Solution:
    
    # Runtime: 93 ms, faster than 84.76% of Python3 online submissions for Sort the Matrix Diagonally.
    # Memory Usage: 14.4 MB, less than 22.21% of Python3 online submissions for Sort the Matrix Diagonally.
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        dictionary = defaultdict(list)
        
        R = len(mat)
        C = len(mat[0])
        
        for i in range (R):
            for j in range (C):
                dictionary[i-j].append(mat[i][j])
                
        
        for i in dictionary:
            heapq.heapify(dictionary[i])
            
    
        for i in range (R):
            for j in range(C):
                mat[i][j] = heapq.heappop(dictionary[i-j])
        
        return mat
    
    
    ''' 
    
    i-j is same for diagonal
    
    
    00  01  02  03  04               0    1    2    3   4
    10  11  12  13  14              -1    0    1    2   3    
    20  21  22  23  24 -----------> -2   -1    0    1   2
    30  31  32  33  34              -3   -2   -1    0   1
    40  41  42  43  44              -4   -3   -2   -1   0
    '''