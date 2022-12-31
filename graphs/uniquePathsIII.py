
# https://leetcode.com/problems/unique-paths-iii/
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:


        R = len(grid)
        C = len(grid[0])

        directions = [
            (0, -1), #left
            (0, 1), #right
            (1, 0), #up
            (-1, 0) #down
        ]

        startrow, startcol, endrow, endcol = 0, 0 ,0, 0

        empty_cell = 0

        for r in range (R):
            for c in range (C):
                if grid[r][c] == 1:
                    startrow, startcol = r, c
                elif grid[r][c] == 2:
                    endrow, endcol = r, c
                elif grid[r][c] == 0:
                    empty_cell += 1

        self.result = 0

        def is_valid(i,j):
            return 0<=i<R and 0<=j<C

        def dfs (i, j , walk ,  visited ):

            if is_valid(i, j):
                for x, y in directions:
                    ix = i+x
                    jy = j+y
                    

                    if is_valid(ix, jy) and (ix, jy) not in visited :
                        if grid[ix][jy] == 2 and  walk == empty_cell:
                            self.result+=1

                        if grid[ix][jy] == 0 :
                            visited.add((ix, jy))
                            dfs(ix, jy, walk+1, visited)
                            visited.remove((ix, jy))

        visited = set()
        visited.add((startrow, startcol))
        dfs(startrow, startcol, 0, visited)
        return self.result

                