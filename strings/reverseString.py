# https://leetcode.com/problems/reverse-string/
class Solution(object):
    
    # Runtime: 196 ms, faster than 58.59% of Python online submissions for Reverse String.
    # Memory Usage: 21.2 MB, less than 26.67% of Python online submissions for Reverse String.
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        
        left = 0
        right = len(s)-1
        
        while left< right :
            s[left],s[right]= s[right],s[left]
            left+=1
            right-=1
        