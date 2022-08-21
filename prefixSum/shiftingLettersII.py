# https://leetcode.com/problems/shifting-letters-ii/

from typing import List
from itertools import accumulate
import operator


class Solution:
    
    # Runtime: 1672 ms, faster than 100.00% of Python3 online submissions for Shifting Letters II.
    # Memory Usage: 39.7 MB, less than 40.00% of Python3 online submissions for Shifting Letters II.
 
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = list("abcdefghijklmnopqrstuvwxyz")
        
        array = [0]* (len(s)+1)
        
        for start, end , direction in shifts:
            addition = (-1 if direction == 0 else 1 )
            array[start] += addition
            array[end+1] += -(addition)
            
            
        array = list(accumulate(array, operator.add))
        
        result = []
        for i in range(len(s)):
            old_chr = ord(s[i])-ord("a")
            new_chr = (old_chr+array[i]) % 26
            result.append(letters[new_chr])

        return "".join(result)  
        