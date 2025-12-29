# https://leetcode.com/problems/design-neighbor-sum-service

class NeighborSum:

    def __init__(self, grid: List[List[int]]):

        self.mappings = defaultdict(tuple)
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])

        for i in range (self.R):
            for j in range (self.C):
                self.mappings[grid[i][j]] = (i,j)

    def isValid(self, i, j):
        return 0<=i<self.R and 0<=j<self.C

    def processor(self, value, directions):
        positionx , positiony = self.mappings[value]
        return sum([self.grid[positionx+a][positiony+b] for a, b in directions if self.isValid(positionx + a , positiony + b)])

    def adjacentSum(self, value: int) -> int:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        return self.processor(value, directions)

    def diagonalSum(self, value: int) -> int:
        directions = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
        return self.processor(value, directions)

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)