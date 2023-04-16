# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])


        dp = [[float("inf")] * C for i in range(R) ]
        spread = set()
        def is_valid(i, j):
            return 0 <= i < R and 0 <= j < C

        direction = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        q = deque([])

        def bfs (q, visited):
            max_level = 0

            while q:
                nx, ny , level = q.popleft()
                dp[nx][ny] = min(level, dp[nx][ny])
                visited.add((nx, ny))
                spread.add((nx, ny))
                if is_valid(nx, ny):
                    for x, y in direction:
                        ix = nx + x
                        jy = ny + y

                        if is_valid(ix, jy) and grid[ix][jy] == 1 and (ix, jy) not in visited:
                            q.append((ix, jy, level+1))
                            max_level = max(max_level, level+1)

            return max_level

        for i in range (R):
            for j in range(C):

                if grid[i][j]==2:
                    q = deque([(i, j, 0)])
                    bfs (q, set())

        fresh_orange_present = False

        for i, j in spread:
            grid[i][j] = 3

        result = 0
        for i in range (R):
            for j in range(C):
                if grid[i][j]==1:
                    fresh_orange_present = True
                elif grid[i][j] == 3:
                    result = max(result, dp[i][j])


        if fresh_orange_present:
            return -1

        return result
