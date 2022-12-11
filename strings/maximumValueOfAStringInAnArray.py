# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

from typing import List
class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        def verify (word):
            try :
                val = int(word)
                return val
            except:
                return len(word)
                
        result = float("-inf") 
        for word in strs:
            result = max(result, verify(word))
            
        return result