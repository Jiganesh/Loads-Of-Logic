# https://leetcode.com/problems/count-common-words-with-one-occurrence/

from typing import List
from collections import Counter

class Solution:

    # Runtime: 182 ms, faster than 34.63% of Python3 online submissions for Count Common Words With One Occurrence.
    # Memory Usage: 14.4 MB, less than 38.37% of Python3 online submissions for Count Common Words With One Occurrence.

    def countWords(self, words1: List[str], words2: List[str]) -> int:        
        
        lookup1 = Counter(words1)
        lookup2 = Counter(words2)
        
        
        words = set(words1 + words2)
        result = 0
        
        for word in words:
            if lookup1[word]==1 and lookup2[word]==1:
                result+=1
        
        return result
    
    
    # One Liner
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        fix = lambda w: set(filter(lambda x: x[1] == 1, Counter(w).items()))

        return len(fix(words1) & fix(words2))
    
    
    # Optimized Single Hashmap

    # Runtime: 69 ms, faster than 97.71% of Python3 online submissions for Count Common Words With One Occurrence.
    # Memory Usage: 14.4 MB, less than 38.37% of Python3 online submissions for Count Common Words With One Occurrence.
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        
        lookup = Counter(words1)
        
        for word in words2:
            if lookup[word]<2:
                lookup[word]-=1
            
        result = 0
        for word, value in lookup.items():
            if value == 0:
                result+=1
        
        return result 