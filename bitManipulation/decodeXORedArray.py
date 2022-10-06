# https://leetcode.com/problems/decode-xored-array/

from typing import List

class Solution:
    # TC : O(N)
    # SC : O(N)
    
    def decode(self, encoded: List[int], first: int) -> List[int]:

        result  = [first]
        xor = first
        for num in encoded:
            xor = xor ^ num
            result.append(xor)
            
        return result 
