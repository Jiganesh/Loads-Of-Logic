# https://leetcode.com/problems/gray-code/

from typing import List


class Solution:
    
    # TC : O(N^2)
    # SC : O(N)
    def grayCode(self, n: int) -> List[int]:

        if n ==0:
            return 0

        result = [0]
        for i in range (0, n):
            result += [(2**i)+ num for num in reversed(result)]
        return result
        