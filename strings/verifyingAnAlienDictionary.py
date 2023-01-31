# https://leetcode.com/problems/verifying-an-alien-dictionary/description
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        lexo = dict(zip(list(order), list('abcdefghijklmnopqrstuvwxyz')))
        
        def transform (word):
            
            return "".join([str(lexo[i]) for i in word])

        a = [transform(i) for i in words]
        return sorted(a)==a
