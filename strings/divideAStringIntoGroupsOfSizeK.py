# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        # we check whether if the string is short and do we need to fill it with fill
        # if the string is short, we add fill to the end of the string
        if len(s)%k !=0 : s+=(k-(len(s)%k)) * fill
            
        # we split the string into k-length pieces
        return[s[i:i+k] for i in range(0,len(s),k)]