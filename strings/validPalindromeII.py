# https://leetcode.com/problems/valid-palindrome-ii/

class Solution(object):
    
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def helper(s):
            return s[::-1]==s
        
        left = 0
        count =0
        right = len(s)-1
        
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return (helper(s[left+1:right+1])  or helper(s[left: right]))
        return True