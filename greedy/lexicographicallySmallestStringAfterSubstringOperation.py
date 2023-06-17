# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution(object):
    def smallestString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        count = 0
        for  ind in range (len(s)):
            if s[ind] != "a" and count == 0:
                count +=1
                while ind < len(s) and s[ind] != "a":
                    s[ind] = chr(ord(s[ind])-1)
                    ind+=1
                
                break
                
        if count  == 0:
            s[-1] = "z"
        
        return "".join(s)
