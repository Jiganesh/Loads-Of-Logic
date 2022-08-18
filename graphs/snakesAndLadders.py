

from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        
        queue = deque()
        queue.append((1,0))
        
        board.reverse()
        
        n = len(board)
        visited = set()
        
        def intToPosition (integer):
            integer = integer-1
            
            row = integer//n
            if row%2==0:
                col = integer%n
            else:
                col = n -1 - (integer%n)
            return row, col
            
        while queue:
            current_position, move = queue.popleft()

            
            for dice_roll in range (1, 7): # possible values of dice roll
                next_position = current_position + dice_roll
                cor_x , cor_y = intToPosition (next_position)
                
                if board[cor_x][cor_y] != -1:
                    next_position = board[cor_x][cor_y]
                    
                if next_position == n*n:
                    return move+1
                
                if next_position not in visited:
                    queue.append((next_position, move+1))
                    visited.add(next_position)
                    
        return -1
    
