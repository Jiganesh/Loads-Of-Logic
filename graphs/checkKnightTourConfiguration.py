# https://leetcode.com/problems/check-knight-tour-configuration/

class Solution(object):

    def checkValidGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        visited = set ()
        
        n = len(grid)
        
        def valid ( x, y):
            return 0<=x<n and 0<=y<n
        
        def get_next_move(cx, cy):
            
            #possible moves from knight
            moves = [
                #top left
                (-1, -2),
                (-2, -1),
                
                # top right
                (-2, 1),
                (-1, 2),
                
                #bottom right
                (1, 2),
                (2, 1),
                
                #bottom left
                (2, -1),
                (1, -2)  
            ]
            
            current_move = grid[cx][cy]
            for x, y in moves:
                nx, ny = cx + x , cy + y 
                if valid(nx, ny) and grid[nx][ny] == current_move + 1:
                    return nx, ny
                
            return -1, -1
                
        def helper(cx, cy):
            nx, ny = get_next_move(cx, cy)
            
            if nx == -1 and ny == -1:
                return
                
            current_move = grid[cx][cy]
            next_move = grid[nx][ny]
            
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                helper(nx, ny)
                
        visited.add((0,0))        
        helper(0,0)
        

        return len(visited)==n*n
        
        
                
            
            
            
            