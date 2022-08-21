# https://leetcode.com/problems/shifting-letters/

from typing import List

class Solution:
    
    # Runtime: 1404 ms, faster than 34.91% of Python3 online submissions for Shifting Letters.
    # Memory Usage: 27.5 MB, less than 47.70% of Python3 online submissions for Shifting Letters.
    
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        s = list(s)
        letters = "abcdefghijklmnopqrstuvwxyz"
        
        prefix_sum = 0
        
        for ind in range (len(s)-1, -1, -1):
            
            prefix_sum += shifts[ind]
            old_char = ord(s[ind]) - ord ("a")
            new_char_ind = (old_char + prefix_sum) % 26
            s[ind] = letters[new_char_ind]
            
        return "".join(s)