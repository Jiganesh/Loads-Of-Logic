# https://leetcode.com/problems/find-and-replace-pattern/

from typing import List

class Solution:
    
    # Runtime: 63 ms, faster than 22.49% of Python3 online submissions for Find and Replace Pattern.
    # Memory Usage: 14 MB, less than 28.72% of Python3 online submissions for Find and Replace Pattern.
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        
        def get_pattern(word):
            hashmap = {}
            string = ""
            for ch in word:
                hashmap[ch]= str(hashmap.get(ch, len(hashmap)))
                string+=hashmap[ch]
                
            return string

        result = []
        compare = get_pattern(pattern)
        for word in words:
            if compare == get_pattern(word) :
                result.append(word)
                
        return result