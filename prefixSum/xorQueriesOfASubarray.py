# https://leetcode.com/problems/xor-queries-of-a-subarray/


from typing import List
from itertools import accumulate
import operator


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        
        prefix_xor = [0]+ list(accumulate(arr, operator.xor))
        
        return [prefix_xor[right+1] ^ prefix_xor[left] for left, right in queries]