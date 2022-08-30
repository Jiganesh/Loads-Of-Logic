# https://leetcode.com/problems/find-the-town-judge/

from typing import List
from collections import defaultdict

class Solution:

    # Runtime: 1242 ms, faster than 40.26% of Python3 online submissions for Find the Town Judge.
    # Memory Usage: 19 MB, less than 27.96% of Python3 online submissions for Find the Town Judge.
    
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_lookup = defaultdict(int)
        
        for person, trusted in trust:
            
            trust_lookup[trusted]+=1
            trust_lookup[person]-=1
            
        for person in range(1, n+1):
            if trust_lookup[person] == n-1:
                return person
        
        return -1
    