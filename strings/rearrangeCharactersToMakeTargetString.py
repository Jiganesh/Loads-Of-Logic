# https://leetcode.com/problems/rearrange-characters-to-make-target-string/
from collections import Counter

class Solution(object):
    
    # Runtime: 36 ms, faster than 100.00% of Python online submissions for Rearrange Characters to Make Target String.
    # Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Rearrange Characters to Make Target String.
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        s = Counter(s)
        target = Counter(target)
        
        minimum = float("inf")
        for i in target:
            
            minimum =  min(s[i]//target[i], minimum)
            
        return minimum
    
    
    # More Pythonic Code
    
    # Runtime: 20 ms, faster than 100.00% of Python online submissions for Rearrange Characters to Make Target String.
    # Memory Usage: 13.6 MB, less than 100.00% of Python online submissions for Rearrange Characters to Make Target String.
    
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        s = Counter(s)
        target = Counter(target)

        return min ([s[i]//target[i] for i in target])