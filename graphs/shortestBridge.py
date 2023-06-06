# https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:


        R = len(grid)
        C = len(grid[0])

        # Step 1 - Find first Island Point
        first_island = set()


        def find_first_island():
            for i in range (R):
                for j in range(C):
                    if grid[i][j]:
                        return (i,j)

        i, j = find_first_island()

        # Find all the points of first Island

        def isvalid(i, j):
            return 0<=i<R and 0<=j<C

        def fip(i, j):

            if isvalid(i,j) and (i,j) not in first_island_points and grid[i][j] == 1:
                grid[i][j] = -1
                first_island_points.add((i,j))
                for x, y in directions:
                    fip(i+x, j+y)

        first_island_points = set()

        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1),
        ]

        fip (i,j)
        
        q = deque([])
        self.min = float("inf")

        for x, y in first_island_points:
            q.append((x, y ,0))

        visited = set(q)
       
        # Move in directions one step at a time
        while q : 
            i, j , steps = q.popleft()

            for x, y in directions:
                ix, jy = x+i, j+y
                if isvalid(ix, jy) and grid[ix][jy] == 1:
                    self.min = min(self.min, steps)
                elif isvalid(ix, jy) and (ix, jy) not in visited and steps < self.min:
                    visited.add((ix,jy))
                    grid[ix][jy] == -1
                    q.append((ix,jy, steps+1))

        return self.min
