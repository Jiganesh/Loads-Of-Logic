# https://leetcode.com/problems/magic-squares-in-grid/



class Solution:

    # TC : O(RC)
    # SC : O(RC)
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def check(i, j):
            summation = sum(grid[i][j:j+3])
            # CHECK FOR ROWS
            for ind in range(i, i+3):
                if sum(grid[ind][j:j+3]) != summation: return False
            # CHECK FOR COLS
            for ind in range(j, j+3):
                if sum(transpose[ind][i:i+3]) != summation: return False
            # CHECK FOR DIAGONAL1
            diagonal_1= grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            if diagonal_1 != summation:
                return False
            # CHECK FOR DIAGONAL2
            diagonal_2= grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
            if diagonal_2 != summation:
                return False
            return True


        R = len(grid)
        C = len(grid[0])

        ans = 0
        transpose = list(map(list, zip(*grid)))

        for i in range(R):
            for j in range(C):
                # CAN MAKE MAGIC SQUARE - FAIL FAST
                if i+2 < R and j+2 < C:
                    # SCAN IF ALL NUMBERS ARE UNIQUE and 1 to 9
                    z = set()
                    for a in range (i, i+3):
                        for b in range(j, j+3):
                            z.add(grid[a][b])
                    if z == set(range(1, 10)):
                        ans += check(i, j)

        return ans