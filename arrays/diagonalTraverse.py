# https://leetcode.com/problems/diagonal-traverse/

from typing import List
from collections import defaultdict

class Solution:
    
    # Runtime: 347 ms, faster than 28.51% of Python3 online submissions for Diagonal Traverse.
    # Memory Usage: 17.2 MB, less than 78.68% of Python3 online submissions for Diagonal Traverse.
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        dictionary = defaultdict(list)
        R, C  = len(mat), len(mat[0])
        
        
        for i in range (R):
            for j in range(C):
                dictionary[i+j].append(mat[i][j])

        result = []    
        for i in range (R-1 +  C-1 + 1):
            if i&1==0:
                dictionary[i].reverse()
            
            result.extend(dictionary[i])
        return result
    
    
    # Runtime: 214 ms, faster than 83.03% of Python3 online submissions for Diagonal Traverse.
    # Memory Usage: 17.1 MB, less than 90.31% of Python3 online submissions for Diagonal Traverse.
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        endrow, endcol = len(mat), len(mat[0])
        
        def go_up(row, col):
            result = []
            while 0<=row<endrow and 0<=col<endcol:
                result.append(mat[row][col])
                row-=1
                col+=1
            return result
        

        result = []
        
        for i in range(endrow):
            result.append(go_up(i, 0))
            
        for i in range (1, endcol):
            result.append(go_up(endrow-1, i))
            
        answer = []
        for ind , ls in enumerate (result):
            answer.extend(ls[::-1] if ind&1 else ls)
        return answer
            