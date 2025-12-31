# https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def valid(x, y):
            return 0<=x<row and 0<=y<col
        
        def reachable (day):
            grid = [[0]* col for _ in range(row)]

            for ind, point in enumerate(cells):
                if ind < day:
                    a, b = point
                    grid[a-1][b-1] = 1

            # top, bottom, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            queue = deque([])
            visited = set()

            for c in range(col):
                if grid[0][c]==0:
                    queue.append((0, c))
                    visited.add((0,c))

            # printing grid 
            # for r in grid: print(*r)
            

            while queue:
                x, y = queue.popleft()

                if x == row-1:
                    return True

                for dx, dy in directions:
                    nx, ny = x+dx , y+dy
                    if valid(nx, ny) and (grid[nx][ny]==0) and ((nx, ny) not in visited):
                        visited.add((nx,ny))
                        queue.append((nx, ny))

            return False

        # Version 1
        # for ind in range (len(cells)):
            # print("Answer", ind, reachable(ind))
            # print("------------")
        

        left = 1
        right = len(cells)
        ans = 0

        while left <= right: 
            mid = (left + right) // 2
            if reachable(mid):
                ans = mid      # mid is a candidate for the LAST day
                left = mid + 1 # try to find a later day
            else:
                right = mid - 1 # too much water, try an earlier day

        return ans