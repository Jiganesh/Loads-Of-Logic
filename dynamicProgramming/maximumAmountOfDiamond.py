"""
Deva give you ad diamond mine of N*M. Each field in this mine contains a positive integer which is the amount of diamond in tons.
Initially the miner is at first column but ccan be at any row. He can move only right , right up, right down from current cell.
The miner can move to the cell diagonally up towards the right or right or diagonally down towards the right.
Yout task is to find out maximum amount of diamond that miner can collect.

Input Format :
First line of input contains two Integers N and M denoting the number of rows and columns
Next N line contains M space separated Integers

Input :
2 2
1 2 3 4

Output:
7
"""

rows, columns = 3,3 # map(int,input().split(" "))
arr = [1,2,5,3,4,6,7,8,9] #list(map(int, input().split(" ")))
mat = [[0]*columns for i in range(rows)]
p=0

for i in range(rows):
    for j in range(columns):
        mat[i][j]=arr[p]
        p+=1
        
def maxcollected(mat, rows, columns):
    dp = [[-1] * (columns+1) for i in range (rows+1)]
    maximum = float('-inf')
    for column in range(columns):
        fromThisPath = helper(dp,mat, rows, columns, column, 0, collected =0)
        maximum = max(maximum, fromThisPath)
    return maximum
        
def helper (dp,mat, rows, columns, i, j, collected=0):
    if valid(i,j, rows, columns) and dp[i][j] != -1: return dp[i][j]
    
    elif (valid(i,j,rows, columns)):
        collected+= mat[i][j]
        collected+= max(helper(dp,mat, rows, columns, i-1, j+1),helper(dp,mat,rows, columns, i+1, j+1),helper(dp,mat, rows, columns, i, j+1 ))
    dp[i][j]= collected
    return collected

def valid (i, j,rows, columns):
    return i<rows and j<columns and i>=0 and j>=0            
            
print(maxcollected(mat,rows, columns)) 
