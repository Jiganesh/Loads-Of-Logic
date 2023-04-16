# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution:
    def addMinimum(self, word: str) -> int:
        
        k = 0
        prev = "z"
        for ch in word:
            if ch <= prev:
                k+=1
            prev = ch
        
        
        return k * 3 - len(word)