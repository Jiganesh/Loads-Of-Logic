# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_lookup = defaultdict(lambda: set())
        cols_lookup = defaultdict(lambda: set())
        identifier_lookup = defaultdict(lambda: set())

        R = len(board)
        C = len(board[0])

        for i in range (R):
            for j in range (C):

                if board[i][j] == ".":
                    continue

                number = board[i][j]
                identifier_row = int(i)//3
                identifier_col = int(j)//3

                if number in rows_lookup[i]:
                    return False
                if number in  cols_lookup[j]:
                    return False
                if number in identifier_lookup[(identifier_row, identifier_col)]:
                    return False
                
                rows_lookup[i].add(number)
                cols_lookup[j].add(number)
                identifier_lookup[(identifier_row, identifier_col)].add(number)

        return True
