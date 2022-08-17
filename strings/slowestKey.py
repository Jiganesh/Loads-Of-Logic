# https://leetcode.com/problems/slowest-key/

import operator
from typing import List

class Solution:
    
    # Runtime: 101 ms, faster than 36.94% of Python3 online submissions for Slowest Key.
    # Memory Usage: 14.1 MB, less than 89.99% of Python3 online submissions for Slowest Key.
    
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        
        for i in range (len(releaseTimes)-1, 0, -1):
            releaseTimes[i] = releaseTimes[i]- releaseTimes[i-1]
            
        result = float("-inf")
        result_ch = ""
        
        for i in range (len(keysPressed)):
            if result < releaseTimes[i]:
                result = max(result , releaseTimes[i])
                result_ch = keysPressed[i]
            if result == releaseTimes[i]:
                result_ch = max(result_ch, keysPressed[i])
                
        return result_ch
    
    # One Liner

    # Runtime: 77 ms, faster than 69.97% of Python3 online submissions for Slowest Key.
    # Memory Usage: 14.2 MB, less than 9.32% of Python3 online submissions for Slowest Key.
    
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str: 
        return max(zip (map(operator.sub, releaseTimes , [0, *releaseTimes]), keysPressed))[1]        