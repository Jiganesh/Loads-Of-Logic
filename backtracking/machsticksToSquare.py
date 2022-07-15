# https://leetcode.com/problems/matchsticks-to-square/

from functools import lru_cache
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        totalSum = sum(matchsticks)
        
        if totalSum%4 != 0: return False
        
        side = totalSum//4
        matchsticks.sort(reverse=True)
        
        @lru_cache
        def helper(l1,l2,l3,l4, index=0):
            
            
            if l1 == l2 ==l3 == l4 == 0 : return True
            
            if l1<0 or l2<0 or l3<0 or l4<0 : return False
            
            if index >= len(matchsticks): return False
            
            
            s = matchsticks[index]
            return helper(l1-s,l2,l3,l4, index+1) or helper(l1,l2-s,l3,l4, index+1) or helper(l1,l2,l3-s,l4, index+1) or helper(l1,l2,l3,l4-s,  index+1)
        
        return helper(side, side, side, side)