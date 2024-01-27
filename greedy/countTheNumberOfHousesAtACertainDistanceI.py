# https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:

        adjacency_matrix = [[float("inf")] * (n+1) for i in range(n+1)]

        #Creating connections
        for house2 in range (2, n+1):
            house1 = house2-1
            adjacency_matrix[house2][house2] = 0
            adjacency_matrix[house1][house1] = 0
            adjacency_matrix[house2][house1] = 1
            adjacency_matrix[house1][house2] = 1

        if x != y:
            adjacency_matrix[x][y] = 1
            adjacency_matrix[y][x] = 1


        for k in range (1, n+1):
            for i in range (1, n+1):
                for j in range(1, n+1):
                    adjacency_matrix[i][j] = min(adjacency_matrix[i][j], adjacency_matrix[i][k] + adjacency_matrix[k][j])

        result = [0] * n
        for i in range (n+1):
            for j in range(n+1):
                if adjacency_matrix[i][j]!=float("inf"):
                    number = adjacency_matrix[i][j]
                    result[number]+=1

        return result[1:] + [0]

