# https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isvalid(i, j):
            return 0<=i<R and 0<=j<C

        def helper(i, j):

            if isvalid(i, j) and board[i][j] == "O":
                board[i][j] = "V"
                # up
                helper(i-1, j)
                # down
                helper(i+1, j)
                # left
                helper(i, j-1)
                # right
                helper(i, j+1)

        R = len(board)
        C = len(board[0])       

        for i in range (R):
            for j in range (C):
                if ((i == 0 or i == R-1)  or (j == 0 or j== C-1)) and  (board[i][j] == "O"):
                    helper(i, j)

        for i in range (R):
            for j in range(C):
                if board[i][j] == "V":
                    board[i][j] = "O"
                else :
                    board[i][j] = "X"