# https://leetcode.com/problems/short-encoding-of-words/

from typing import List

class Solution:
    
    # Runtime: 173 ms, faster than 82.33% of Python3 online submissions for Short Encoding of Words.
    # Memory Usage: 14.5 MB, less than 92.09% of Python3 online submissions for Short Encoding of Words.
    
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        
        s = set(words)
        ans = 0
        
        for w in words:
            for i in range(1,len(w)):
                
                # discard is used because if its not present i will not get error
                s.discard(w[i:])
        
        for i in s:
            ans += len(i)
            
        return ans+len(s)
    
    
        