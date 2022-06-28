# https://leetcode.com/problems/convert-1d-array-into-2d-array/

from typing import List

class Solution:
    # Runtime: 1014 ms, faster than 96.23% of Python3 online submissions for Convert 1D Array Into 2D Array.
    # Memory Usage: 21.3 MB, less than 95.27% of Python3 online submissions for Convert 1D Array Into 2D Array.
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if len(original) != m*n : return []
        
        return [original[i: i+n] for i in range (0,len(original),n)]
    
    
    