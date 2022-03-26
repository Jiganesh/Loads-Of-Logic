# https://leetcode.com/problems/maximum-repeating-substring/

class Solution(object):
    
    # Runtime: 12 ms, faster than 97.33% of Python online submissions for Maximum Repeating Substring.
    # Memory Usage: 13.5 MB, less than 66.67% of Python online submissions for Maximum Repeating Substring.
    
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        
        repeatingWordCount = 1
        while word*repeatingWordCount in sequence:
            ans+=1
            
        return ans-repeatingWordCount