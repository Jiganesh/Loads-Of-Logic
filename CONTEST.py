import bisect, heapq, operator
from typing import List
from itertools import accumulate
from collections import defaultdict, Counter, deque
import math

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        for i in grid:
            print(*i)
       
print(Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]))
print(Solution().checkXMatrix([[6,0,0,0,0,0,0,18],[0,17,0,0,0,0,18,0],[0,0,13,0,0,17,0,0],[0,0,0,9,18,0,0,0],[0,0,0,2,20,0,0,0],[0,0,20,0,0,3,0,0],[0,14,0,0,0,0,11,0],[19,0,0,0,0,0,0,9]]
))