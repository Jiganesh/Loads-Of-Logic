# https://leetcode.com/problems/game-of-life/
# https://www.youtube.com/watch?v=l2mkUZG6CLU&ab_channel=CodingDecoded

class Solution:
    
    # Solution Using Extra Space
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        
        newMatrix = [[0]* len(board[0]) for i in range (len(board))]
    
        def value (i , j):
            
            if (i>=0 and i < len(board)) and (j >=0 and j < len(board[i])):
                return board[i][j]
            else:
                return 0
            
            
        
        for i in range (len(board)):
            for j in range (len(board[i])):
        
                val = sum ([value(i-1,j-1), value(i-1,j),value(i-1,j+1), value(i,j-1), value(i,j+1), value(i+1,j-1),value(i+1,j),value(i+1,j+1)])
                                
                if board[i][j] and val<2 or val >3: # case 1 and case 3
                    val = 0
                elif (board[i][j] and (val ==2 or val ==3)): # case 2
                    val=1
                elif val ==3: # case 4
                    val =1
                else:
                    val = board[i][j]
                    
                newMatrix[i][j]= val
                
        for i in range (len(board)):
            for j in range (len(board[i])):
                board[i][j]= newMatrix[i][j]
        
        
    # TC : O(M*N)
    # SC : O(1)

    # Runtime: 36 ms, faster than 85.68% of Python3 online submissions for Game of Life.
    # Memory Usage: 13.9 MB, less than 51.25% of Python3 online submissions for Game of Life.
    
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [[-1,-1],  [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        
        
        # returns count of live cell also considers future dead cells
        def liveNeighbors(r, c):
            liveCount = 0
            
            for i in directions:
                dr = r+i[0]
                dc = c+i[1]
                
                if valid(dr, dc) and (board[dr][dc]==1 or board[dr][dc]==-2):
                    liveCount+=1
                    
            return liveCount

        # checks if cell is valid or not
        def valid ( r, c):
            return 0<=r and  r <rows and 0<=c and c < columns
            
        
        
        # - 2 means the cell will change to dead cell from live cell
        # 2 means the cell will change to live cell from dead cell
        
        
        rows = len(board)
        columns = len(board[0])
        
        for i in range (rows):
            for j in range (columns):
                
                liveCount = liveNeighbors(i, j)
                
                if board[i][j]== 1 :
                    if (liveCount<2 or liveCount >3):  # case1 and case3
                        board[i][j] = -2
                    elif (liveCount == 2 or liveCount==3): # case2
                        board[i][j] =1
                else:
                    if liveCount==3: # case4
                        board[i][j] = 2
                        
        for i in range (rows):
            for j in range (columns):
                
                if board[i][j]==-2:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=1
                
            
            
        
        