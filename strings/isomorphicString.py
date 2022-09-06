# https://leetcode.com/problems/isomorphic-strings/

from collections import defaultdict

class Solution:
    
    # Runtime: 48 ms, faster than 84.04% of Python3 online submissions for Isomorphic Strings.
    # Memory Usage: 14.2 MB, less than 88.72% of Python3 online submissions for Isomorphic Strings.

    def isIsomorphic(self, s: str, t: str) -> bool:
        
        
        # AS s and t will have same length given in constraints
        n = len(s)
        lookups = defaultdict(str)
        lookupt = defaultdict(str)
        
        
        for ind in range (n):
            chs = s[ind]
            cht = t[ind]
            
            if chs in lookups and lookups[chs]!= cht:
                return False
            if cht in lookupt and lookupt[cht]!= chs:
                return False
            
            lookups[chs]=cht
            lookupt[cht]=chs

        return True