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
