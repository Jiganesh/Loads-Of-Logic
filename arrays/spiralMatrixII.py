#https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(n):
        x,y=0,-1
        row,col,dirr=n,n,1
        
        mat=[[None for i in range(n)] for i in range(n)]
        value=1
        while row>0 and col>0:
            for i in range(col):
                y+=dirr
                mat[x][y]=value
                value+=1
            row-=1
            
            for i in range(row):
                x+=dirr
                mat[x][y]=value
                value+=1
            col-=1
            
            dirr*=-1

        return mat

    def generateMatrix(self, n: int) :

        value=1
        matrix=[[None for i in range(n)] for i in range(n)]
        startm,endm=0,n
        startn,endn=0,n
        while startm<endm and startn<endn:
            for i in range(startn, endn):       #moving left to right through column
                matrix[startm][i]=value         #row will be decided by startm ie top
                value+=1
            startm+=1                           #top row will move downward to crop the matrix
            for i in range(startm, endm):       #moving top to bottom through m rows
                matrix[i][endn-1]=value         #column will be const and is right end endn, and to avoid out of bound index -1
                value+=1
            endn-=1                             #matrix be cropped by shifting rightmost end towards left

            for i in range(endn-1, startn-1, -1):       #moving right to left through column
                matrix[endm-1][i]=value                 #row will be decided by endm ie bottom
                value+=1
            endm-=1                                     #bottom row will move upward to crop the matrix
            for i in range(endm-1, startm-1,-1):        #moving bottom to top through m rows
                matrix[i][startn]=value                 #column will be const and is left end startn
                value+=1
            startn+=1                                   #matrix be cropped by shifting leftmost end towards right

        return matrix

    # Submitted by Jiganesh
    
    # Runtime: 34 ms, faster than 84.21% of Python3 online submissions for Spiral Matrix II.
    # Memory Usage: 13.9 MB, less than 85.84% of Python3 online submissions for Spiral Matrix II.
    def generateMatrix(self, n: int):
        
        
        matrix = [[0]*n for i in range (n)]
        
        pointer = 1
        
        startRow, endRow = 0, n
        startCol, endCol = 0, n
        
        while pointer <= n*n:
            
            # traversing Right
            
            for i in range (startCol, endCol):
                matrix[startRow][i] = pointer
                pointer+=1    
            startRow+=1 
            
            # traversing Down
            for i in range (startRow, endRow):
                matrix[i][endCol-1]= pointer
                pointer+=1
            endCol-=1
            
            # traversing Left
            
            for i in range (endCol-1, startCol-1,-1):
                matrix[endRow-1][i]= pointer
                pointer+=1
            endRow-=1
            
            # traversing Up
            
            for i in range (endRow-1, startRow-1,-1):
                matrix[i][startCol]= pointer
                pointer+=1
            startCol+=1
            
        return matrix
            


print(generateMatrix(3))