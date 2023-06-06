# https://leetcode.com/problems/sudoku-solver/

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """


        R = len(board)
        C = len(board[0])

        def is_valid(r, c, num,  board):
            
            nr = (r//3)*3
            nc = (c//3)*3

            for row in range (R):
                if board[row][c]== num:
                    return False
                
            for col in range (C):
                if board[r][col]==num:
                    return False

            for i in range (max(R, C)):
                cr = nr + i//3
                cc = nc + i% 3
                if board[cr][cc] == num:
                    return False
            return True

        
        def solve(board):

            for r in range (R):
                for c in range (C):

                    if board[r][c]==".":
                        for num in range (1, 10):
                            s = str(num)

                            if is_valid(r, c, s, board):
                                board[r][c]=s
                                if solve(board):
                                    return True
                                else:
                                    board[r][c] = "."
                        return False
            return True

        solve(board)