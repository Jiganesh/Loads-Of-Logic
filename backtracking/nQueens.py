# https://leetcode.com/problems/n-queens/
from typing import List


class Solution:
    
    # Runtime: 61 ms, faster than 87.63% of Python3 online submissions for N-Queens.
    # Memory Usage: 14.4 MB, less than 82.22% of Python3 online submissions for N-Queens.
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

"""

00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
30 31 32 33 34
40 41 42 43 44

"""

"""
`valid_configs` contains configurations of n queens that satisfy
threat constraints.

Each element in `queens` represents the position of a queen.
Its row is indicated by the element *index* and its column is
indicated by the element *value*. Given this, duplicate values
in `queens` would mean two rows had a queen in the same column,
which isn't allowed.

yx_diffs and yx_sums both represent diagonals that are threatened
by a queen in `queens`. As shown below, diagonals can be represented
with a single integer calculated from the difference or sum of a
position's row and columns indices. Differences (row - col) are
left->right diagonals and sums are right->left diagonals.

yx_diffs (row_idx - col_idx):
3 |  3  2  1  0
2 |  2  1  0 -1
1 |  1  0 -1 -2
0 |  0 -1 -2 -3
r  ------------
    c  0  1  2  3

yx_sums (row_idx + col_idx):
3 |  3  4  5  6
2 |  2  3  4  5
1 |  1  2  3  4
0 |  0  1  2  3
r  ------------
    c  0  1  2  3
"""