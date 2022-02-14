# https://leetcode.com/problems/find-the-difference/


class Solution(object):
    
    # TC :O(N)
    # SC :O(N)
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dict = {i : s.count(i) for i in s}
        
        for i in t:
            if i not in dict or dict[i]==0:
                return i
            else:
                dict[i]-=1
        