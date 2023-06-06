# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        s = sentence.split(" ")
        
        for i in range (len(s)):
            if s[i-1][-1]!=s[i][0]:
                return False
        return True
            