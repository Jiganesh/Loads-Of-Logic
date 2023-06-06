# https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        r, v = 0, 0

        for ind , row in enumerate(mat):
            if row.count(1) > v:
                r = ind
                v = row.count(1)
                
        return [r, v]