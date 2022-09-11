# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:

    # Runtime: 211 ms, faster than 82.48% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    # Memory Usage: 14.7 MB, less than 97.94% of Python3 online submissions for Maximum Number of Vowels in a Substring of Given Length.
    def maxVowels(self, s: str, k: int) -> int:
        
        vowelCount = 0
        max_vowelCount = 0
        
        for ind , ch in enumerate(s):
            
            if ind>=k and  s[ind-k] in "aeiou":
                vowelCount-=1
            
            if s[ind] in "aeiou":
                vowelCount+=1

            max_vowelCount = max(max_vowelCount, vowelCount)
            
        return max_vowelCount
    
