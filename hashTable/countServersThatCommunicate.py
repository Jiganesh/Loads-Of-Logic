class Solution:
    def countServers(self, grid: List[List[int]]) -> int:


        R = len(grid)
        C = len(grid[0])

        row_dict = defaultdict(int)
        col_dict = defaultdict(int)


        total_servers = 0

        for i in range (R):
            for j in range (C):
                if grid[i][j]:
                    row_dict[i] += 1
                    col_dict[j] += 1
                    total_servers += 1
                

        for i in range(R):
            for j in range(C):
                if grid[i][j] and row_dict[i] == 1 and col_dict[j] == 1:
                    total_servers -=1

        return total_servers





        