# https://leetcode.com/problems/delete-columns-to-make-sorted/

from typing import List

class Solution:
    # Complexity: O(C * RLOGR) where C is the number of columns and R is the number of rows
    
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        for col in zip(*strs):
            sorted_col = sorted(col)
            result += list(col) != sorted_col

        return result

