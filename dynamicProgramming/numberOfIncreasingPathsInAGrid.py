# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:



        R = len(grid)
        C = len(grid[0])

        MOD = 10**9 + 7

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        dp = {}
        

        def isvalid(i, j):
            return 0<=i<R and 0<=j<C

        def helper(i, j):

            if (i, j) in dp:
                return dp[(i,j)]
                

            if not isvalid(i, j): 
                return 0

            temp = grid[i][j]
            grid[i][j] = -1

            ans = 1
            for x , y in directions:
                ni = x + i
                nj = y + j

                if isvalid(ni, nj) and grid[ni][nj] > temp:
                    ans = ans + helper(ni, nj)

            grid[i][j] = temp
            ans = ans % MOD

            dp[(i, j)] = ans
            return ans


        count = 0
        for i in range(R):
            for j in range (C):
                count += helper(i , j)

        return count % MOD