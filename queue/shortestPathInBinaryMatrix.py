# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import *

class Solution:
    

    def shortestPathBinaryMatrix(self, grid) -> int:
    
        n = len (grid)
        
        q = deque()
        
        if grid[0][0]==1 or grid[-1][-1] ==1:
            return -1
        
        
        q.append([0,0])
        s = set((0,0))
        level =0
        
        while q :
                                        
            level+=1
            qlen = len(q)
            print(q)
            
            for _ in range(qlen):
                i, j = q.popleft()
                
                
                if i==n-1 and j==n-1:
                    return level
                
                for ii in range (i-1,i+2):
                    for jj in range(j-1,j+2):
                        
                        if  0<=ii<n and 0<=jj<n  and grid[ii][jj]==0:
                            grid[ii][jj]=1
                            q.append([ii,jj])

            
        return -1
        