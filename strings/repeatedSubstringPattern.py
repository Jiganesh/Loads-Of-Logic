# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)
        
        for ind in range (1,n):
            substring = s[:ind]
            formedString = substring * (n// ind)

            if formedString == s :
                return True
        return False


    def repeatedSubstringPattern(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1