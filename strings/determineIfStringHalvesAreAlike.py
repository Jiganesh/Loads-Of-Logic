# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        leftvowels, rightvowels = 0, 0 
        left , right = 0, len(s)-1

        vowels = "aeiouAEIOU"
        while left < right:
            if s[left] in vowels:
                leftvowels+=1
            if s[right] in vowels:
                rightvowels+=1
            
            left+=1
            right-=1
        
        return leftvowels==rightvowels

