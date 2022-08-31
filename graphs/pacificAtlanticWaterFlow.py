# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import List
class Solution:
    
    # Runtime: 424 ms, faster than 59.54% of Python3 online submissions for Pacific Atlantic Water Flow.
    # Memory Usage: 15.8 MB, less than 21.64% of Python3 online submissions for Pacific Atlantic Water Flow.

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R = len(heights)
        C = len(heights[0])
        
        pacific = [[False]*C for _ in range(R)]
        atlantic = [[False]*C for _ in range(R)]
        
        def valid (i, j, visited):
            return 0 <=i< R and 0<=j <C and visited[i][j]==False
        
        def dfs(i, j, visited):

            visited[i][j]=True
            
            for dirx, diry in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                
                if valid(i+dirx, j+diry, visited) and heights[i+dirx][j+diry] >= heights[i][j]:
                    
                    dfs(i+dirx, j+diry, visited, heights[i][j])
            

        for col in range (C):
            
            dfs(0, col, pacific)
            dfs(R-1, col, atlantic)
            
        for row in range (R):
            
            dfs(row, 0, pacific)
            dfs(row, C-1, atlantic)
        
        result = []
        for i in range (R):
            for j in range(C):
                
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
                    
        return result 
    

    # Pythonic Code Using Set Intersection
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R = len(heights)
        C = len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def valid (i, j, visited):
            return 0 <=i< R and 0<=j <C and (i, j) not in visited
        
        def dfs(i, j, visited):

            visited.add((i,j))
            
            for dirx, diry in [(-1,0), (1, 0), (0, -1), (0, 1)]:
                
                if valid(i+dirx, j+diry, visited) and heights[i+dirx][j+diry] >= heights[i][j]:
                    
                    dfs(i+dirx, j+diry, visited)
            

        for col in range (C):
            
            dfs(0, col, pacific)
            dfs(R-1, col, atlantic)
            
        for row in range (R):
            
            dfs(row, 0, pacific)
            dfs(row, C-1, atlantic)
        
        return list(pacific & atlantic)