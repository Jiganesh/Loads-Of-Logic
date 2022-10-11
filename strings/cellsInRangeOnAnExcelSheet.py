# Problem Link: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start = s[0]
        end = s[3]
        res = []
        for i in range(ord(start),ord(end)+1):
            for j in range(int(s[1]), int(s[4])+1):
                temp = chr(i)  + str(j)
                res.append(temp)
        return res