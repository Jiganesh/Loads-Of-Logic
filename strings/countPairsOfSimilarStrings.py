# https://leetcode.com/problems/count-pairs-of-similar-strings/

from typing import List
from collections import defaultdict


class Solution:
    # TC : O(N * W Log W) where N is the number of words and W is the length of the word
    # SC : O(N)
    def similarPairs(self, words: List[str]) -> int:
        result = 0 
        lookup = defaultdict(int)

        for word in words:
            identifier = tuple(sorted(set(word)))
            if identifier in lookup:
                result += lookup[identifier]
            lookup[identifier]+=1
        return result 

    # Without Sorting
    
    # TC : O(N * W) where N is the number of words and W is the length of the word
    # SC : O(N)
    def similarPairs(self, words: List[str]) -> int:

        def record_alphabet (word):
            alphabet = [0]*26
            for alpha in word:
                index = ord(alpha)-ord("a")
                alphabet[index] |= 1
            return alphabet

        result = 0 
        lookup = defaultdict(int)

        for word in words:
            identifier = tuple(record_alphabet(word))
            if identifier in lookup:
                result += lookup[identifier]
            lookup[identifier]+=1
        return result 
